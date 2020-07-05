import pandas as pd
import numpy as np

df = pd.DataFrame({ "A": [2, 1, 1, 2, 2], "B": [False, np.nan, False, np.nan, False]})
print(df)
print(df.groupby('A')['B'].count())

