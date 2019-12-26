import pandas as pd

df = pd.DataFrame({'A': [10, 15, 65, 54, 51, 96],
                   'B': [1, 2, 3, 2, 2, 1]})

df['1st quartile'] = df.groupby('B')['A'].transform(lambda x: x.quantile(0.25)).round(2)
df['2nd quartile'] = df.groupby('B')['A'].transform(lambda x: x.quantile(0.50)).round(2)
df['3rd quartile'] = df.groupby('B')['A'].transform(lambda x: x.quantile(0.75)).round(2)
df['quantile'] = pd.qcut(df['B'], 3, labels=False).values
df['items'] = pd.cut(df['B'], bins=3).value_counts()


print(df)