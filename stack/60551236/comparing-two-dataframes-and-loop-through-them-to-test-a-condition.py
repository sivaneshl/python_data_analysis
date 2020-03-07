import pandas as pd
import numpy as np

df1 = pd.DataFrame([[2020,'1/1/2020',123],[2020,'1/1/2020',345],[2020,'10/1/2020',123],[2020,'11/13/2020',123]],
                   columns=['Year','Date','ID'])
df2 = pd.DataFrame([[2020,'2020-01-01  00:00:00','2020-02-01  00:00:00',123],
                    [2020,'2020-01-01  00:00:00','2020-01-02  00:00:00',123],
                    [2020,'2020-03-01  00:00:00','2020-05-01  00:00:00',978],
                    [2020,'2020-09-21  00:00:00','2020-10-01  00:00:00',978]],
                   columns=['Year','BeginDate','EndDate','ID'])
df2['BeginDate'] = pd.to_datetime(df2['BeginDate'])
df2['EndDate'] = pd.to_datetime(df2['EndDate'])
df1['Date'] = pd.to_datetime(df1['Date'])
# df1['condition'] = np.where((df1['Year']==df2['Year'])&(df1['ID']==df2['ID']),True, False)
# &((df1['Date']>=df2['BeginDate'])or(df1['Date']<=df2['EndDate']))

# df1.reset_index(inplace=True)
# df2.reset_index(inplace=True)

date_range = list(zip(df2['BeginDate'],df2['EndDate']))
# print(date_range)

def check_date(date):
    # print(date)
    for (s,e) in date_range:
        if date>=s and date<=e:
            return True
    return False

df1['condition'] = (df1['Year'].isin(df2['Year']))&(df1['ID'].isin(df2['ID']))
df1['date_compare'] = df1['Date'].apply(lambda x: check_date(x))
df1['condition'] = (df1['condition']==True)&(df1['date_compare']==True)
# df1['date_compare'] = df1.apply(
#     lambda df: (
#         True if (df['Date'].between(i,j) for (i,j) in date_range)
#         else False
#     ), axis=1
# )


# &((df1['Date']>=df2['BeginDate'])&(df1['Date']<=df2['EndDate']))
# df1['condition'] = (df1['condition']==True)&(df1['ID'].isin(df2['ID']))
# df1['condition'] = (df1['condition']==True)&(df1['Date'].between(df2['BeginDate'], df2['EndDate']))
print(df2)
print(df1)