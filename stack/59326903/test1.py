import pandas as pd

level = list(map(int, list('111112222')))
company = list('XXYYYXXXY')
item = list('ababcabca')
value = [100,200,35,150,35,48,100,50,80]
col = ['Level', 'Company', 'Item', 'Value']
df = pd.DataFrame([level,company,item,value]).T
df.columns = col

df1 = (df.groupby(['Level', 'Company', 'Item'])['Value'].sum())
df2 = (df1.sum(level=0).to_frame().assign(Company='total').set_index('Company', append=True))
df3 = (df1.groupby(['Level','Company']).sum().to_frame().assign(Item='total').set_index('Item', append=True))

# print(df1.to_frame())
# print(df2)
# print(df3)
#
# dfx = pd.concat([df1.to_frame(),
#                  (df1.sum(level=0).to_frame().assign(Level='total').set_index('Level', append=True)),
#                  (df1.groupby(['Level','Company']).sum().to_frame().assign(Company='total').set_index('Company', append=True))
#                  ]).sort_index()

dfx = pd.concat([df1.to_frame(), df2, df3]).sort_index()
# dfx = pd.concat([df1.to_frame().reset_index(),
#                  df2.reset_index(),
#                  df3.reset_index()],sort=True).reset_index(drop=True)
print(dfx)
