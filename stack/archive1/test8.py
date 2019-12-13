import pandas as pd
import numpy as np

df = pd.DataFrame([['A',np.NaN],['B',np.NaN], ['C',np.NaN], [np.NaN,'D'], [np.NaN,'E'], [np.NaN,'F']],
                  columns=['COL1','COL2'])
df['COL1'] = df['COL1'].fillna(df['COL2'])
df = df.drop(columns='COL2')
print(df)