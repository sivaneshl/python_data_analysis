import pandas as pd
import numpy as np

df = pd.DataFrame({'i_example': [0, 3, 3, 0, 0, 1, 1, 2, 2],
                   'i_frame': [20, 13, 13, 21, 21, 22, 22, 20, 20],
                   'OId': [3.0, np.NaN, np.NaN, 3.0, 3.0, 0.0, np.NaN, 0.0, 1.0],
                   'HId': [0.0, 8.0, 10.0, np.NaN, 0.0, 4.0, 4.0, 4.0, 4.0]})
print(df)

dup1 = df[df.duplicated(['i_example', 'i_frame', 'OId'], keep=False) & df['OId'].notna()]
dup2 = df[df.duplicated(['i_example', 'i_frame', 'HId'], keep=False) & df['HId'].notna()]
print(dup1)
# print(pd.concat([dup1, dup2]))

dupes = (df['OId'].notna() & df.duplicated(['i_example', 'i_frame', 'OId'], keep=False)) | (df['HId'].notna() & df.duplicated(['i_example', 'i_frame', 'HId'], keep=False))
invalid_df = df[dupes]
valid_df = df[~dupes]
print(valid_df)
print(invalid_df)