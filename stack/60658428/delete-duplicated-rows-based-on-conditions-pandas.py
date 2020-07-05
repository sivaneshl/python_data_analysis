import pandas as pd

d = {'id': ["i1", "i2", "i3", "i4"], 'x1': [13, 13, 61, 61], 'x2': [10, 10, 13, 13], 'x3': [12, 12, 2, 22], 'x4': [24, 24,9, 12]}
df = pd.DataFrame(data=d)
print(df.loc[df.duplicated(['x2','x3','x4']), 'id'])
print(df.drop_duplicates(subset=['x1','x2','x3','x4'], keep='first'))