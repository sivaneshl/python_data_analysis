import pandas as pd

def convert_percentage(percentage):
    return float(percentage.rstrip('%'))

df = pd.read_csv('test.csv', converters={'Reduction': convert_percentage})
print(df)
# df['Reduction'] = df['Reduction'].str.rstrip('%').astype('float')
new_df = df.groupby('Category')['Reduction'].agg(min=min).reset_index()
new_df['min'] = new_df['min'].astype(str)+'%'
print(new_df)