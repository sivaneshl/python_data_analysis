import pandas as pd

df = pd.DataFrame({'date':['2014-09']})

print(pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d %H:%M:%S.000'))