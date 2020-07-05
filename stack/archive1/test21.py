import pandas as pd

df1 = pd.DataFrame({'var1': [1], 'var4': ['P']})
df2 = pd.DataFrame({'var2': list('abcd'), 'var3': range(4)})

print(df1)
print(df2)

# solution1
print(pd.concat((df1,df2),axis=1).ffill())

# solution 2
# print(df1.iloc[0].to_dict())
print(df2.assign(**df1.iloc[0].to_dict()))