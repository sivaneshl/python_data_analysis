import pandas as pd
import numpy as np

df = pd.DataFrame({'Date': ['2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05', '2018-01-08',
                            '2018-01-09', '2018-01-10', '2018-01-11', '2018-01-12', '2018-01-15'],
                   'signal': [0,0,0,1,0,0,0,1,1,0],
                   'positions': [np.NaN, 0.0, 0.0, 1.0, -1.0, 0.0, 0.0, 1.0, 0.0, -1.0],
                   'rates': [1.2065, 1.2023, 1.2065, 1.2045, 1.1973, 1.1932, 1.1992, 1.2017, 1.2137, 1.22]})
df = df.set_index('Date')


entryRate = 0.0
for i, row in df.iterrows():
    if row['positions'] == 1.0:
        entryRate = row['rates']
        df.loc[i,'entryRate'] = entryRate
    elif row['positions'] == -1.0:
        df.loc[i,'entryRate'] = entryRate
        entryRate = 0.0
    else:
        df.loc[i,'entryRate'] = entryRate

print(df)



