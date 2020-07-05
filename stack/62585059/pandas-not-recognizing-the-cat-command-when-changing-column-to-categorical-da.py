import pandas as pd
import numpy as np

df = pd.DataFrame({'i_example': [0, 3, 3, 0, 0, 1, 1, 2, 2],
                   'i_frame': [20, 13, 13, 21, 21, 22, 22, 20, 20],
                   'OId': [3.0, np.NaN, np.NaN, 3.0, 3.0, 0.0, np.NaN, 0.0, 1.0],
                   'HId': [0.0, 8.0, 10.0, np.NaN, 0.0, 4.0, 4.0, 4.0, 4.0]})
print(df)

cat_columns = ['OId', 'HId']
df[cat_columns] = df[cat_columns].astype('category')
df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)
# for col in cat_columns:
#     df[col] = df[col].cat.codes

print(df)