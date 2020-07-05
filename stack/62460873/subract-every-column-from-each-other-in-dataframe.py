import pandas as pd
import numpy as np
import itertools

df = pd.DataFrame(np.random.randint(0, 5, size=(5, 4)), columns=list('ABCD'))

for comb in (list(itertools.combinations(df.columns, r=2))):
    df[comb] = (df[comb[0]] - df[comb[1]])

print(df)

