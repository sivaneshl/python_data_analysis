import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

ix = pd.DatetimeIndex(['2019-12-25', '2019-12-28', '2019-12-31', '2020-01-03'])
df = pd.DataFrame({'col': [1, 1, 1, 1]}, index=ix)
# df = df.resample('D').asfreq()
print(df.resample('W').sum())