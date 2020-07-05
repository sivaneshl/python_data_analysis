import pandas as pd

df = pd.DataFrame({'name': ['A','D','M','T','B','C','D','E','A','L'],
                   'id': [1,1,1,2,2,3,3,3,3,5],
                   'rate': [3.5,4.5,2.0,5.0,4.0,1.5,2.0,2.0,1.0,5.0]})

print(df)

print(df.groupby(by='id').mean())
df = df[df.groupby(by='id')['rate'].transform('mean')>3]
print(df)

