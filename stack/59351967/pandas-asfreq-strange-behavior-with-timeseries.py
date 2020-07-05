import pandas as pd

df = pd.read_csv('url_inflation.csv')
df['date'] = pd.to_datetime(df.date, yearfirst=True, format='%Y-%m')
df.set_index('date', inplace=True)
print(df.index)

# df = df.sort_index().asfreq(freq='AS')
df = df.resample('AS').agg('sum')

print(df)


