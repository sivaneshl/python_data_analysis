import pandas as pd
import numpy as np

df = pd.read_csv('C:/python_data_analysis/resources/course1_downloads/census.csv')
print(df.head())
df_copy=df

def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    # return pd.Series({'min': np.min(data), 'max': np.max(data)})
    row['min'] = np.min(data)
    row['max'] = np.max(data)
    return row

df=df.apply(min_max, axis=1)
# the axis parameter is really the parameter of the index to use
# to apply to all rows pass 1
print(df.head())

# using lambda
columns=['POPESTIMATE2010',
         'POPESTIMATE2011',
         'POPESTIMATE2012',
         'POPESTIMATE2013',
         'POPESTIMATE2014',
         'POPESTIMATE2015']
print(df_copy.apply(lambda x: np.min(x[columns]), axis=1))
# print(df_copy.head())
