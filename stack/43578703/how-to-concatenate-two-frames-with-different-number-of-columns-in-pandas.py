import pandas as pd

df1 = pd.DataFrame({'property_id':[1,2],
                    'beds':[1,2]}).set_index(['property_id','beds'])
df2 = pd.DataFrame({'property_id':[3,4]}).set_index('property_id')

print(pd.concat([df1,df2]).sort_index())
