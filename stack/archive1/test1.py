import pandas as pd
import numpy as np


df = pd.DataFrame([[np.NaN, np.NaN, 1.0, 1.0, 1.0],
                   [np.NaN, 2.0, 2.0, 1.0, 1.0],
                   [np.NaN, 3.0, 4.0, 2.0, 1.0],
                   [np.NaN, 1.0, 1.0, 1.0, 1.0],
                   [np.NaN, 1.0, 1.0, 1.0, 1.0]],
                  columns=['apr_12', 'may_12', 'jun_12', 'jul_12', 'aug_12'])
# print(np.where(~df.loc[0].isnull())[0][0])
for i, row in df.iterrows():
    print(np.where(~row.isnull())[0][0])

# df['first_index'] = (np.where(~df.isnull())[0][0])
print(np.where(~df.isna()))
# df['first_index'] = np.where(df.loc[df.index.values].isnull())[0][0]
data = [
    ['1245', np.nan, np.nan, 1.0, 1.0, ''],
    ['1246', np.nan, 1.0, 1.0, 1.0, ''],
    ['1247', 1.0, 1.0, 1.0, 1.0, ''],
    ['1248', 1.0, 1.0, np.nan, np.nan, ''],
    ['1249', np.nan, 1.0, np.nan, 1.0, '']
]

df = pd.DataFrame(data, columns = ['city_code', 'apr_12', 'may_12', 'jul_12', 'aug_12', 'first_index'])
col_list = ['apr_12', 'may_12', 'jul_12', 'aug_12']
df['first_index'] = df[col_list].apply(lambda x: (np.where(~x.isnull())[0][0]), axis=1)
print(df)