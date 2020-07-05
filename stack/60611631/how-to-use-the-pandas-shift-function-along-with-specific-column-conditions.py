import pandas as pd
import numpy as np

df = pd.DataFrame([['2019-05-03T06:00:00.000Z', 3.125, 0.000, '10B', 1.0],
                   ['2019-05-03T18:00:00.000Z', 2.975, 0.000, '10B', 1.0],
                   ['2019-05-04T06:00:00.000Z', 2.825, 0.000, '10B', 0.5],
                   ['2019-05-04T18:00:00.000Z', 2.675, 0.000, '10B', 0.0],
                   ['2019-05-05T06:00:00.000Z', 2.525, 0.000, '10B', 0.5]],
                  columns=['timestamp', 'first_actual', 'first_required', 'location', 'first_initial_pass'])

df['first_final'] = np.where((df['first_initial_pass']!=0.5), df['first_initial_pass'],
                             np.where((df['first_initial_pass'].shift(1)==1.0)&
                                      (df['first_initial_pass'].shift(2)==1.0),
                                      1, 0))

                             #
                             # (np.where(df['first_initial_pass']==0.5)&
                             #  (df['first_initial_pass'].shift(1)==1.0)&
                             #  (df['first_initial_pass'].shift(2)==1.0),
                             #  1, 0))

print(df)