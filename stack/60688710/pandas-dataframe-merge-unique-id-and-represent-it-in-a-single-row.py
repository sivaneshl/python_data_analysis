import pandas as pd
import numpy as np

df = pd.DataFrame({'ID': [1,1,1,1,2,2,2,2],
                   'Data': ['a','b','c','d','a','b','c','d'],
                   'col3': range(1,9)})
df = df.set_index(['ID','Data'])
df.drop('col3', axis=1, inplace=True)
print(df)