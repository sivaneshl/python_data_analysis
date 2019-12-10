import pandas as pd
import numpy as np

df1 = pd.DataFrame([['Bob','V434',50.00],['Jill','E333',22.11],['Hank','B442',11.11]],
                   columns=['Name','ID','Amount'])

df2 = pd.DataFrame([['Bob','V434','E333','B442'],
                    ['Karen','V434','E333','B442'],
                    ['Jill','V434','E333','B442'],
                    ['Hank','V434','E333','B442']],
                   columns=['Name','ID_First','ID_Second','ID_Third'])

# print(pd.concat([df1.merge(df2, left_on=['ID','Name'], right_on=['ID_First','Name']),
#                  df1.merge(df2, left_on=['ID', 'Name'], right_on=['ID_Second', 'Name']),
#                  df1.merge(df2, left_on=['ID', 'Name'], right_on=['ID_Third', 'Name'])])[['Name','ID','Amount']])


new_df = pd.DataFrame()
for col in ['ID_First', 'ID_Second', 'ID_Third']:
  df = pd.merge(df1, df2, left_on=['ID','Name'], right_on=[col,'Name'], how='inner')
  new_df = df if new_df.empty else new_df.append(df)

print(new_df)