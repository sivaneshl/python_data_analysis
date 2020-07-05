import pandas as pd
import math
import numpy as np

ix = pd.DatetimeIndex(['2019-12-25', '2019-12-28', '2019-12-31', '2020-01-03'])
df = pd.DataFrame({'col': [1, 1, 1, 1]}, index=ix)
# df = df.resample('D').asfreq()
df['day'] = ((pd.to_datetime(df.index) - pd.to_datetime('19700101')) / np.timedelta64(1, 'D')).astype(int) - 3
df['week'] = df['day'].apply(lambda x: int(x / 7))
print(df)
