import pandas as pd

df1 = pd.DataFrame({'Date1': ['01-01-2019', '02-01-2019', '03-01-2019', '04-01-2019', '05-01-2019'],
                    'City': ['city1', 'city2', 'city3', 'city4', 'city5'],
                    'Country': ['country1', 'country1', 'country1', 'country2', 'country2'],
                    'Location': ['loc1', 'loc2', 'loc3', 'loc4', 'loc5']})
df2 = pd.DataFrame({'Date2': ['01-01-2019', '03-01-2019', '05-01-2019'],
                    'City': ['city1', 'city3', 'city5'],
                    'Country': ['country1', 'country1', 'country2'],
                    'Location': ['loc1', 'loc3', 'loc5']})

df1['Date1'] = pd.to_datetime(df1['Date1'])
df2['Date2'] = pd.to_datetime(df2['Date2'])

df3 = pd.merge_asof(df1.sort_values('Date1', ascending=True),
                    df2.sort_values('Date2', ascending=True),
                    left_on='Date1',
                    right_on='Date2',
                    by=['Country', 'City', 'Location'],
                    direction='forward').fillna(method='ffill')

print(df3)