import pandas as pd
import numpy as np

df = pd.DataFrame({'id': [4, 2, 1, 1, 3],
                   'col1': [150, np.NaN, 96,  233, 194],
                   'col2': [np.NaN, 177,  301, 81, np.NaN],
                   'col3': [287, 138, 90, np.NaN, 402]})

df_group = pd.DataFrame({'id': [0, 1, 2, 3, 4],
                         'col1': [200, 171, 318, 284, 377],
                         'col2': [133, 125, 428, 334, 501],
                         'col3': [346, 400, 261, 195, 238]})
df_group.set_index('id', inplace=True)

for col in df.columns[1:]:
    df[col] = np.where(df[col].isnull(), df['id'].map(df_group[col]), df[col])

print(df)

