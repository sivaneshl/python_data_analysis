import pandas as pd
import numpy as np

df = pd.read_csv('C:/python_data_analysis/resources/course1_downloads/census.csv')
df = df[df['SUMLEV']==50]
print(df.head())

# calculate the average CENSUS2010POP by state
for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
    print(state, avg)

# using groupby
# groupby returns the grouping key and the resulting dataframe
for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print(group, avg)


# groupby using a function
# first set the field we want to group by as the index
df=df.set_index('STNAME')

def fun(item):
    if item[0] < 'M':
        return 0
    if item[0] < 'Q':
        return 1
    return 2

for group, frame in df.groupby(fun):
    print(group, len(frame))


# groupby aggregate
df = pd.read_csv('C:/python_data_analysis/resources/course1_downloads/census.csv')
df = df[df['SUMLEV']==50]
print(df.groupby('STNAME').agg({'CENSUS2010POP':np.average}))


# sum and average using groupby agg
# here agg is applied on a series
print(df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg':np.average, 'sum':np.sum}))
# level = 0 indicates the first index (in a single index or multi index)
# level = n indicates the nth level index in a multi index

# agg on a df
print(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
      .agg({'avg': np.average, 'sum': np.sum}))

# using the agg column labels as the same name as the columns
print(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
      .agg({'POPESTIMATE2010':np.average, 'POPESTIMATE2011':np.sum}))