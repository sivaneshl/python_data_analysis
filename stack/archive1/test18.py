import pandas as pd

df = pd.DataFrame({"X1":["a","b","c"], "X2":["b","c","d"], "X3":[500,200,10]})
df['ID'] = df.index
print(df)
randomset1 = df.sample(1)
randomset2 = df.sample(1)
print(randomset1)
print(randomset2)
print(pd.merge(randomset1, randomset2, how='inner', on='ID'))