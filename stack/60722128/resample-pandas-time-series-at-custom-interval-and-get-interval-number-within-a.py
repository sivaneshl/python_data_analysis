import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 500)

np.random.seed(123)
df = pd.DataFrame({'time': pd.date_range('2005-01-01', '2007-12-31', freq='1D'),
                   'NDVI': np.random.randn(1095)})
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d')
df.set_index('time', inplace=True)

df['res'] = df.index.dayofyear // 10
print(df)

def assign_group_interval(year_grp):
    year_grp['period'] = year_grp.groupby(pd.Grouper(freq='10D'), as_index=False)\
        .apply(lambda x: x['NDVI'])\
        .index.get_level_values(0)
    # year_grp['period'] = temp_df.index.get_level_values(0)
    return year_grp

df.groupby(df.index.year).apply(assign_group_interval).reset_index()