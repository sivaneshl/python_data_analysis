import pandas as pd
import numpy as np

df1 = pd.DataFrame([[2019, '2019-01-01 00:00:00', 's904112'],
                    [2019, '2019-01-01 00:00:00', 's911243'],
                    [2019, '2019-01-01 00:00:00', 's917131'],
                    [2019, '2019-01-01 00:00:00', 'sp986214'],
                    [2019, '2019-01-01 00:00:00', 's510006'],
                    [2020, '2020-01-10 00:00:00', 's540006']],
                   columns=['Year','Date','ID'])
df2 = pd.DataFrame([[2020, '2020-01-27  00:00:00', '2020-09-02  00:00:00', 's904112'],
                    [2020, '2020-01-27  00:00:00', '2020-09-02  00:00:00', 's904112'],
                    [2020, '2020-01-03  00:00:00', '2020-03-15  00:00:00', 's904112'],
                    [2020, '2020-04-15  00:00:00', '2020-01-05  00:00:00', 's904112'],
                    [2020, '2020-01-05  00:00:00', '2020-05-15  00:00:00', 's540006'],
                    [2019, '2019-01-05  00:00:00', '2019-05-15  00:00:00', 's904112']],
                   columns=['Year','BeginDate','EndDate','ID'])
df2['BeginDate'] = pd.to_datetime(df2['BeginDate'])
df2['EndDate'] = pd.to_datetime(df2['EndDate'])
df1['Date'] = pd.to_datetime(df1['Date'])

df1['condition'] = False
for idx1, row1 in df1.iterrows():
    match = False
    for idx2, row2 in df2.iterrows():
        if (row1['Year']==row2['Year']) & \
                (row1['ID']==row2['ID']) & \
                (row1['Date']>=row2['BeginDate']) & \
                (row1['Date']<=row2['EndDate']):
            match = True
            break
    df1.at[idx1, 'condition'] = match

print(df1[['Year', 'Date', 'ID']])
print(df2)
print(df1)