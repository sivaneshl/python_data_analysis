import numpy as np
import pandas as pd

df = pd.DataFrame([[1,'wi@gn.c.',20,'26-11-19 12.06.36.726000'],
                   [2,'wi@gn.c.',40,'26-12-19 12.06.37.293000'],
                   [3,'by@gn.c.',50,'26-11-19 12.06.37.960000'],
                   [4,'wi@gn.c.',20,'26-01-20 12.06.51.306000'],
                   [5,'wi@gn.c.',60,'26-02-20 12.06.52.458000'],
                   [6,'by@gn.c.',15,'26-08-19 12.06.58.397000'],
                   [7,'wi@gn.c.',37,'26-12-19 12.07.00.191000'],
                   [5,'wi@gn.c.',60,'26-02-20 12.06.52.458000'],
                   [6,'by@gn.c.',15,'26-08-19 12.06.58.397000'],
                   [7,'wi@gn.c.',37,'26-12-19 12.07.00.191000']],
                  columns=['ID','Email','Amount','Date'])

# convert your 'Date' to datetimeindex
df['Date'] = pd.to_datetime(df['Date'], format = '%d-%m-%y %H.%M.%S.%f')
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)
print(df)
end = pd.datetime.now()
# print(end - pd.DateOffset(months=1), end)
# print((df.loc['2020-02-12 23:49:17': '2020-03-12 23:49:17']))
df_1mo = df.loc[end - pd.DateOffset(months=1): end].groupby('Email')['Amount'].agg(total_1mo=np.size)
df_3mo = df.loc[end - pd.DateOffset(months=3): end].groupby('Email')['Amount'].agg(total_3mo=np.size)
df_6mo = df.loc[end - pd.DateOffset(months=6): end].groupby('Email')['Amount'].agg(total_6mo=np.size)

# merge all 3 dfs on 'Email'
print(df_1mo.merge(df_3mo, on='Email', how='outer').merge(df_6mo, on='Email', how='outer').fillna(0))