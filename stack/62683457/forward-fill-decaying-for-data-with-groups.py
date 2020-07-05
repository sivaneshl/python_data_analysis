import pandas as pd
import numpy as np
df = pd.DataFrame({'A': [np.nan, 1, np.nan, np.nan, 14, np.nan, 14, 9, np.nan, np.nan],
                   'g': ['a', 'b', 'a', 'b', 'a','b','a', 'b', 'a', 'b']})
df.index = ['2015','2015','2016','2016','2017','2017','2018','2018','2019','2019']
df.index = pd.to_datetime(df.index)
df.index = df.index.rename('time')

# df['A'] = df.reset_index().groupby('g')['A'].transform(lambda x: x)
# print(df)

print(
    df.reset_index().groupby('g')['A'].transform(lambda x: x.fillna(method='ffill')/2 if x.isnull() else x)
)

# print(
#     df.reset_index().groupby('g')['A'].apply(lambda x: (x, type(x)))
# )

# print(df.groupby(df[['g', 'A']], as_index=False)['A']
#       .transform(lambda x: x.ffill()/2))