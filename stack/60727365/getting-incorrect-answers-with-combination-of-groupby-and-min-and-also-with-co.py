import pandas as pd

df = pd.DataFrame({'Date': ['14-06-1995', '15-06-1995', '16-06-1995', '17-06-1995', '18-06-1995', '19-06-1995', '20-06-1995'],
                   'Category': ['A1', 'A1', 'A1', 'A2',  'A2', 'A3', 'A3'],
                   'Reduction': ['-1.91%', '-1.32%', '-12.34%', '-2.12%', '-1.78%', '-1.24%', '-1.20%']})
df['Reduction'] = df['Reduction'].str.rstrip('%').astype('float')
new_df = df.groupby('Category')['Reduction'].min()
print(new_df)