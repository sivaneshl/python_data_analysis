import numpy as np
import pandas as pd
from difflib import SequenceMatcher

df = pd.DataFrame({"id":[9,12,13,14],
                   "text":["Error number 609 at line 10", "Error number 609 at line 22", "Error string 'foo' at line 11", "Error string 'bar' at line 14"]})
print(df)

#cross join with filter onl text column
df = df.assign(a=1).merge(df[['text']].assign(a=1), on='a')
#filter out same columns per rows
df = df[df['text_x'] != df['text_y']]
#sort columns per rows
df[['text_x','text_y']] = pd.DataFrame(np.sort(df[['text_x','text_y']],axis=1), index=df.index)
#remove duplicates
df = df.drop_duplicates(subset=['text_x','text_y'])
#get similarity
df['r'] = df.apply(lambda x: SequenceMatcher(None, x.text_x, x.text_y).ratio(), axis=1)
#filtering
df = df[df['r'] > 0.8].drop(['a','r'], axis=1)

print(df)