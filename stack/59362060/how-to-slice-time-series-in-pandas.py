import pandas as pd

df = pd.DataFrame([['2018-01-01',5.0,'a'],
                   ['2018-01-01',10.0,'a'],
                   ['2018-01-02',2.0,'c'],
                   ['2018-01-04',10.0,'b'],
                   ['2018-01-06',20.0,'a']],
                  columns=['date','value','customers'])
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df.groupby(df.index.to_period('M'))['customers'].nunique()