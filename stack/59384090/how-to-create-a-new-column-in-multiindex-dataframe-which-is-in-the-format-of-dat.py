import pandas as pd

df1 = pd.DataFrame([['2019-12-2', 20, 'a1'],
                    ['2019-12-2', 30, 'a2'],
                    ['2019-12-2', 40, 'a3'],
                    ['2019-12-2', 50, 'a4'],
                    ['2019-12-2', 60, 'a5'],
                    ['2019-12-3', 20, 'd1'],
                    ['2019-12-3', 30, 'd2'],
                    ['2019-12-3', 40, 'd3'],
                    ['2019-12-3', 50, 'd4'],
                    ['2019-12-3', 60, 'd5'],
                    ['2019-12-4', 20, 'g1'],
                    ['2019-12-4', 30, 'g2'],
                    ['2019-12-4', 40, 'g3'],
                    ['2019-12-4', 50, 'g4'],
                    ['2019-12-4', 60, 'g5']],
                   columns=['date', 'delta_mins', 'sold_before'])
df1['date'] = pd.to_datetime(df1['date'])
# print(df1['date'].dtype)
df1 = df1.groupby(['date', 'delta_mins', 'sold_before']).agg(lambda x: x)
df1 = df1.reset_index(drop=True)
df1['actual_time'] = pd.to_datetime(df1['date'].dt.strftime('%Y-%m-%d') + ' 10:30:00') - df1['delta_mins'].apply(lambda x:  pd.Timedelta(minutes=x))
# df1 = df1.groupby(['date', 'delta_mins', 'sold_before']).agg(lambda x: x)
print(df1)



