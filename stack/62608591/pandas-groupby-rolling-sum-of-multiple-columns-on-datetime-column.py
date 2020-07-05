import pandas as pd

df = pd.DataFrame({"column1": range(6),
                   "column2": range(6),
                   'group': 3*['A', 'B'],
                   'date':pd.date_range("20190101", periods=6)})

print(df)
print(df.rolling('3d', on='date')['column1'])
print((df.groupby('group').rolling("1d", on='date')['column1'].sum()).groupby('group').shift(fill_value=0))

# df = df.reset_index().rename(columns={df.index.name: 'index'})
# print((df.groupby(['group', 'index']).rolling("4D", on='date')[['column1', 'column2']].sum()).groupby('group').shift(fill_value=0).reset_index())