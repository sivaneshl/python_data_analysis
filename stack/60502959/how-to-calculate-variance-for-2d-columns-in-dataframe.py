import pandas as pd

d = {'id': range(1,13),
     'lat': [62, 47, 55, 74, 31, 77, 85, 63, 42, 32, 71, 57],
     'long': [89, 87, 67, 55, 47, 72, 76, 79, 44, 92, 99, 69]}

df = pd.DataFrame(d)

df['var'] = df[['lat','long']].var(axis=1)
print(df)