import pandas as pd
import numpy as np

df1 = pd.DataFrame([[2020, '2020-01-01', 123],
                    [2020, '2020-01-01', 123],
                    [2020, '2020-01-01', 345],
                    [2020, '2020-01-10', 123],
                    [2020, '2020-11-13', 123]],
                   columns=['Year','Date','ID'])
df2 = pd.DataFrame([[2020,'2020-01-15  00:00:00','2020-02-01  00:00:00',123],
                    [2020,'2020-01-01  00:00:00','2020-01-02  00:00:00',123],
                    [2020,'2020-03-01  00:00:00','2020-05-01  00:00:00',978],
                    [2020,'2020-09-21  00:00:00','2020-10-01  00:00:00',978]],
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



# if np.logical_and((year == row['Year']),
#                   (id == row['ID']),
#                   (date >= row['BeginDate']),
#                   (date <= row['EndDate'])):
#     return True

# df1['condition'] = check_match(df1['Year'], df1['Date'], df1['ID'])
print(df1[['Year', 'Date', 'ID']])
print(df2)
print(df1)