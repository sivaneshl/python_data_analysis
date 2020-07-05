import pandas as pd
import numpy as np

df = pd.DataFrame({'BIN': [111, 222,333,444,111,123],
                   'ISSUER': ['adam', 'mike','mickey','jana',np.NaN, np.NaN]})

df_unique = df.groupby(by=[['BIN','ISSUER']])['BIN','ISSUER']
print(df_unique)

df['ISSUER'] = df['ISSUER'].fillna(df['BIN'])
print(df)