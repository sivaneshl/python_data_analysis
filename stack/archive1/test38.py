import pandas as pd
import datetime as dt

df1 = pd.DataFrame([['2019-12-11 12:00:16.599',1],
                    ['2019-12-11 12:00:16.17',2],
                    ['2019-12-11 12:00:17.11',3 ]],
                   columns=['datetime','ValueDF1'])
df2 = pd.DataFrame([['2019-12-11 12:00',4 ]],
                   columns=['datetime','ValueDF2'])

df1['datetime'] = pd.to_datetime(df1['datetime'])
df2['datetime'] = pd.to_datetime(df2['datetime'])

# df1['datetime_min'] = pd.to_datetime([dt.datetime.strftime(d, "%Y-%m-%d %H:%M") for d in df1["datetime"]])
# print(df1.merge(df2,left_on='datetime_min', right_on='datetime', how='left'))

print(
    pd.merge_asof(df1.sort_values('datetime'), df2.sort_values('datetime'))
)