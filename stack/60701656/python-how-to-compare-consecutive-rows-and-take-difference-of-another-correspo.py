import pandas as pd
import numpy as np

df = pd.DataFrame([['ABC','NE','XYZ','2020-03-01','2020-01-02',161,'dc_input'],
                   ['ABC','NE','XYZ','2020-03-01','2020-01-02',130,'dc_input'],
                   ['ABC','NE','XYZ','2020-03-01','2020-01-03',167,'dc_input'],
                   ['ABC','NE','XYZ','2020-03-01','2020-01-03',158,'dc_input'],
                   ['PQR','SE','GHQ','2020-03-01','2020-01-04',115,'dc_input'],
                   ['PQR','SE','GHQ','2020-03-01','2020-01-04',100,'dc_input']],
                  columns=['dc','region','banner','input_date','week','qty','general'])

compare_cols = ['dc','region','banner','input_date','week','general']


df = df.sort_values(by=['dc','region','banner','input_date','week','qty','general'])
# df = df.set_index(['dc','region','banner','input_date','week','general'])
df2 = df.set_index(compare_cols).groupby(compare_cols)['qty'].diff().dropna().reset_index()
df2['general'] = 'sub_output'
print(df2)

df = (df.reset_index().merge(df2, how='outer').drop('index', axis=1))
print(df)