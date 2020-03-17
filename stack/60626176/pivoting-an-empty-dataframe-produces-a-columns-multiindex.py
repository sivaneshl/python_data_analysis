import pandas as pd
df = pd.DataFrame({'type': ['A', 'A', 'A'], 'val': [1, 2, 3], 'col': ['a', 'b', 'a'], 'ind': [6, 6, 8]})

df1 = pd.DataFrame(columns=['a', 'b', 'c', 'd'], index=[6, 7, 8])

df2 = df1.merge(df[df['type'] == 'A'][['val', 'col', 'ind']].pivot_table(values='val', index='ind', columns='col', fill_value=0),
                left_index=True, right_index=True, how='left', suffixes=('','_y')).fillna(0.0)

df3 = df1.merge(df[df['type'] == 'B'][['val', 'col', 'ind']].pivot_table(values='val', index='ind', columns='col', fill_value=0),
                left_index=True, right_index=True, how='left').fillna(0.0)

df2['a'], df2['b'] = df2['a_y'], df2['b_y']
df2 = df2.drop(['a_y', 'b_y'],1)
print(df2)
print(df3)