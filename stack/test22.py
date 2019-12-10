import pandas as pd

df = pd.DataFrame({'OldIndex': [0,1,2,3,4],
                'c1':['00', '01', '02', '03', '04']}).set_index('OldIndex')
myindex = pd.Index(['I1','I2','I3'])
df = df.iloc[:len(myindex)].set_index(myindex)

print(df)