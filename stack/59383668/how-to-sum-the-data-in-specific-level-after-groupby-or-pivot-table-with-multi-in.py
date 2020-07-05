import pandas as pd
import numpy as np

df = pd.DataFrame({'A': ['a','a','b','b'],
                   'B': ['c','d','e','f'],
                   'C': [1,1,1,1]})


# df['D'] = np.arange(4)
# print(df)

grp1 = df.groupby('A')
grp2 = df.groupby(['A','B'])

print(grp1.get_group('a').sum())
print(grp2.sum())