import pandas as pd
import numpy as np

df1 = pd.DataFrame([[np.NaN, 1, np.NaN],
                    [np.NaN, np.NaN, 10],
                    [3, np.NaN, 6],
                    [np.NaN, np.NaN, np.NaN],
                    [np.NaN, np.NaN, np.NaN]],
                   columns=['A', 'B', 'C'],
                   index=['aaa', 'bbb', 'ccc', 'ddd', 'eee'])
df2 = pd.DataFrame([[1, 1, np.NaN],
                    [np.NaN, np.NaN, 10],
                    [np.NaN, 1, np.NaN]],
                   columns=['A', 'B', 'C'],
                   index=['aaa', 'bbb', 'eee'])

print(df1.fillna(df2))