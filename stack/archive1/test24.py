import pandas as pd
import numpy as np

df = pd.DataFrame([['17:35',101.1,102,100,101,75],
                   ['18:42',101,105,101,103,75],
                   ['18:56',103,108,102,107,50],
                   ['19:45',107,105,101,103,50],
                   ['20:01',103,104,101,102,50]],
                  columns=['Time','Open','High','Low','Close','NumberOfTrades'])

dd = {'Time':'first',
      'Open':'first',
      'High':'max',
      'Low':'min',
      'Close':'last',
      'NumberOfTrades':'sum'}

df['grp'] = (df['NumberOfTrades'].cumsum() % 150).eq(0)[::-1].cumsum()
df = df.groupby(by='grp', sort=False)[['Time','Open','High','Low','Close','NumberOfTrades']].agg(dd).reset_index(drop=True)

print(df)
