import pandas as pd
import numpy as np

df = pd.DataFrame([['ABC', 1, 0, 0],
                   ['DEF', 2, 0, 0],
                   ['GHI', 3, 0, 0],
                   ['JKL', 4, 0, 2],
                   ['MNO', 5, 0, 2],
                   ['PQR', 6, 0, 2],
                   ['STU', 7, 0, 0]],
                  columns=['Date & Time', 'column 1', 'column 2', 'column 3'])

df['new'] = np.where(df['column 3'] == 2, df['column 1'] - df['column 1'].shift(1) * 5, 0)

print(df)