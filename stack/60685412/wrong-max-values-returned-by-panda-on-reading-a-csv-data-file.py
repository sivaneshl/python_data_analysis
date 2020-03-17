import pandas as pd

df = pd.DataFrame({'Date': ['03/13/2020', '03/12/2020', '03/11/2020', '03/10/2020',
                            '03/09/2020', '03/06/2020', '03/05/2020', '03/04/2020'],
                   'Close/Last': ['$277.97', '$248.23', '$275.43', '$285.34', '$266.17','$289.03', '$292.92', '$302.74'],
                   'Volume': [92683030, 104618500, 64094970, 71322520, 71686210, 56544250, 46893220, 54794570]})

df['Date'] = pd.to_datetime(df['Date'])
df['Close/Last'] = df['Close/Last'].apply(lambda x: x[1:]).astype(float)
print(df['Close/Last'].max())
print(df['Date'].max())