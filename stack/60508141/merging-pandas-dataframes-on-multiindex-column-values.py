import pandas as pd
df1 = pd.DataFrame({'col1':[1,1,2,2],'col2':[10,10,20,20]})
df1.columns = pd.MultiIndex.from_product([['df1_labels'],df1.columns])

print(df1)

df2 = pd.DataFrame({'col3':[100,200],'col4':[10,20]})
df2.columns = pd.MultiIndex.from_product([['df2_labels'],df2.columns])

print(df2)

df3 = pd.merge(df1,df2,
               left_on=[('df1_labels','col2')], right_on=[('df2_labels','col4')])
print(df3)