import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 5, size=(5, 1)), columns=list('A'))
print(df)

minx = np.min(df).values[0]
maxx = np.max(df).values[0]
np.arange(minx,maxx,0.1)


