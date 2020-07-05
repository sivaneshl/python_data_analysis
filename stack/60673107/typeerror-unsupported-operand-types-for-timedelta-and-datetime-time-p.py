import pandas as pd
import datetime

time_interval = datetime.timedelta(minutes=5)
df_time_size = pd.DataFrame({'time': ['12:00:00']})
df_time_size.loc[:, 'time'] = (df_time_size.loc[:, 'time'] + time_interval)
print(df_time_size)

