import pandas as pd
import numpy as np

s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])
# cateogrize into 3 bins
print(pd.cut(s, 3))
# You can also add labels for the sizes [Small < Medium < Large].
print(pd.cut(s, 3, labels=['Small', 'Medium', 'Large']))

# cut dataframe
df = pd.read_csv('C:/python_data_analysis/resources/course1_downloads/census.csv')
df = df[df['SUMLEV']==50]
df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({('avg', np.average)})
print(pd.cut(df['avg'], 10, labels=[*range(1,11)]))

