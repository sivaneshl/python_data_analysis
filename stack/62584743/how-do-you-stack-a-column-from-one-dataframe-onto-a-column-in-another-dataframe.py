import pandas as pd
import numpy as np

rng = pd.date_range('2020-01', periods=5, freq='M')
df1 = pd.DataFrame({ 'Date': rng, 'Val' : np.random.randn(len(rng)), 'Val2': ['a', 'b', 'c', 'd', 'e']})
rng2 = pd.date_range('2020-07', periods=5, freq='M')
df2 = pd.DataFrame({ 'Date': rng2, 'Val' : np.random.randn(len(rng))})

print(pd.concat([df1, df2], ignore_index=True))
