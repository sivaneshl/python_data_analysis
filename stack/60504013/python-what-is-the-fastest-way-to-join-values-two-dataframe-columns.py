import pandas as pd

df = pd.DataFrame({1: {0: 'a', 1: 'a', 2: 'a'},
 2: {0: 'b', 1: 'b', 2: 'b'},
 3: {0: 'c', 1: 'c', 2: 'c'}})

print(df)

print(df.apply(lambda x: ' '.join(x),axis=1))