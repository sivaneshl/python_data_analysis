import pandas as pd

level = list(map(int, list('111112222')))
company = list('XXYYYXXXY')
item = list('ababcabca')
value = [100,200,35,150,35,48,100,50,80]
col = ['Level', 'Company', 'Item', 'Value']
df = pd.DataFrame([level,company,item,value]).T
df.columns = col

# soln 1
df1 = (df.groupby(['Level', 'Company', 'Item'])['Value'].sum().unstack())
df1 = (df1.assign(total=df1.sum(1)).stack().to_frame('Value'))
# print(df1)


# soln 2
df1 = (df.groupby(['Level', 'Company', 'Item'])['Value'].sum())
# print(df1.to_frame())
# print(df1.sum(level=0).to_frame().assign(Level='total').set_index('Level', append=True))
# print(df1.groupby(['Level','Company']).sum().to_frame().assign(Company='total').set_index('Company', append=True))

df2 = (pd.concat([df1.to_frame(),
                  (df1.sum(level=0).to_frame().assign(Level='total').set_index('Level', append=True)),
                  (df1.groupby(['Level','Company']).sum().to_frame().assign(Company='total').set_index('Company', append=True))
                  ]).sort_index())
print(df2)

