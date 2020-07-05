import pandas as pd
import numpy as np

df = pd.DataFrame({'id': [1,2,3,4,5,6,3,4,5],
                   'col1': [9, np.NaN, 4,  7, np.NaN, 3, 4,  7, np.NaN],
                   'col2': [2, 4,  3, np.NaN, 3, np.NaN, 5, 6, np.NaN],
                   'col3': [np.NaN, 4,  np.NaN, np.NaN, 3, 8, np.NaN, 4, 2]})
print(df)

df_group1 = df.groupby('id')[['col1']].sum()
df_group2 = df.groupby('id')[['col2']].sum()
df_group3 = df.groupby('id')[['col3']].sum()
df_group = pd.concat([df_group1, df_group2, df_group3], axis = 1)
for i in df['id'].unique():
    df_group = df_group/len(df[df['id'] == i])
print(df_group)

for col in df.columns[1:]:
    df[col] = np.where(df[col].isnull(), df['id'].map(df_group[col]), df[col])
# df['col1'] = np.where(df['col1'].isnull(), df['id'].map(df_group['col1']), df['col1'])
# df['col2'] = np.where(df['col2'].isnull(), df['id'].map(df_group['col2']), df['col2'])
# df['col3'] = np.where(df['col3'].isnull(), df['id'].map(df_group['col3']), df['col3'])

print(df)
