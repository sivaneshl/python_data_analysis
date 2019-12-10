import pandas as pd

df = pd.DataFrame([['A235',[1,3,4,6,8]],['A537',[3,5,2,7,8]]], columns=['Num','ID'])
print(df)
# randomset1=df.sample(1)
# randomset2=df.sample(1)
# print(set(randomset1['ID']))
# print(set(randomset2['ID']))
# print([id for id in randomset1['ID'].tolist() if id in randomset2['ID'].tolist()])

randomset1=set(df.loc[0]['ID'])
randomset2=set(df.loc[1]['ID'])
# randomset1=df.sample(1)
# randomset2=df.sample(2)
# print(set(randomset1['ID']).intersection(set(randomset2['ID'])))
print(randomset1.intersection(randomset2))
print(randomset1&randomset2)

