import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 10000)

vals = [['1.00.00.00', 'Total Assets', 1000], ['1.01.00.00', 'Cash', 200], ['1.02.00.00', 'Inventory', 800], ['1.02.01.00', 'Goods in process', 300], ['1.02.02.00', 'Goods for sale', 500], ['2.00.00.00', 'Liabilities', 750], ['2.01.00.00', 'Commercial Liabilities', 700], ['2.02.00.00', 'Other liabilities', 50], ['3.00.00.00', 'Net equity', 250]]
cols = ['account', 'name', 'balance']
df = pd.DataFrame(vals, columns=cols)

sub_account_cols = ['sub_account_1', 'sub_account_2', 'sub_account_3', 'sub_account_4']
clasif_cols = ['clasif_1', 'clasif_2', 'clasif_3', 'clasif_4']

df['sub_account_1'] = df['sub_account_2'] = df['sub_account_3'] = df['sub_account_4'] = ''
df['clasif_1'] = df['clasif_2'] = df['clasif_3'] = df['clasif_4'] = np.NaN
df['level'] = 0

for idx, row in df.iterrows():
    sub_accounts = row['account'].split('.')
    df.loc[idx, sub_account_cols] = sub_accounts
    for i, sub_account in enumerate(sub_accounts):
        if sub_account=='00':
            df.loc[idx, 'level'] = i
            df.loc[idx, 'clasif_' + str(i)] = row['name']
            break

for i, clasif_col in enumerate(clasif_cols):
    df[clasif_col] = df.groupby('sub_account_'+str(i+1))[clasif_col].apply(lambda x: x.fillna(method='ffill')).fillna('')

df['last_level'] = np.where(df['level']>=df['level'].shift(-1), True, False)
df.loc[len(df)-1, 'last_level'] = True

df.drop(sub_account_cols, axis=1, inplace=True)
print(df)

