import pandas as pd
from nltk.tokenize import TweetTokenizer

df = pd.DataFrame([['an apple is red', 'pop is here'],['pear  is green', 'see is blue']], columns=['A', 'B'])

df['A'] = [TweetTokenizer().tokenize(text) for text in df['A']]
df['id'] = [1, 2]
print(df['A'])
for k in df['A']:
    print(k)
    for item in k:
        pid = df[df['A']==item]['id']
        print(pid)


