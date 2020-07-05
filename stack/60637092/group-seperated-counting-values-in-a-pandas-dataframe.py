import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, np.NaN, 3, np.NaN, np.NaN, 1, 2, np.NaN, 3],
                   'B': [10, 20, 5, 1, 2, 3, 10, 50, 80, 5]},
                  index=range(10))
print(df.dropna().groupby('A')['B'].min())