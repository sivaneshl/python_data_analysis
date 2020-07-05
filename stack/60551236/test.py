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

date_range = list(zip(df2['BeginDate'],df2['EndDate']))
# print(date_range)

def check_date(date):
    for (s,e) in date_range:
        if date>=s and date<=e:
            return True
    return False

df1['allinone'] = (df1['Year'].isin(df2['Year']))&(df1['ID'].isin(df2['ID']))&(df1['Date'].apply(lambda x: check_date(x)))


df1['condition'] = (df1['Year'].isin(df2['Year']))&(df1['ID'].isin(df2['ID']))
df1['date_compare'] = df1['Date'].apply(lambda x: check_date(x))
df1['final'] = (df1['condition']==True)&(df1['date_compare']==True)

print(df2)
print(df1)