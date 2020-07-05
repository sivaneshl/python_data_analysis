import pandas as pd
import numpy as np
import calendar

pd.set_option('display.max_rows', 200)

df = pd.DataFrame({'date': pd.date_range('01/01/2019', '12/31/2020', freq='D')})
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month.apply(lambda x: calendar.month_abbr[x])
df['week'] = df['date'].dt.week.map("{:02}".format)
df['yr_wk_mth'] = df['year'].astype(str) + ' / Week ' + df['week'] + ' / ' + df['month']

print(df.groupby(['year','week']).last())