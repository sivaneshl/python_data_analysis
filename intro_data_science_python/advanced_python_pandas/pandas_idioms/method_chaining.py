import pandas as pd
df = pd.read_csv('C:/python_data_analysis/resources/course1_downloads/census.csv')
print(df.head())

# method chaining
print(df.where(df['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
    .head())