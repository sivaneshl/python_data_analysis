import pandas as pd

df = pd.DataFrame([['E001','xyz',[{"codeTs":"12345567 ","goodsAttrName":"test1"},{"codeTs":"6402910000","goodsAttrName":"test2"}],'mmm','nnn','zzz','aaa'],
                   ['E002','1234','','123','jjj','iii','bb']],
                  columns=['EMP_ID','ATTR1_OLD_VAL','ATTR1_NEW_VAL','ATTR2_OLD_VAL','ATTR2_NEW_VAL','ATTR3_OLD_VAL','ATTR3_NEW_VAL'])
print(df)
df = df.explode('ATTR1_NEW_VAL')
print(pd.concat([df.drop(['ATTR1_NEW_VAL'], axis=1), df['ATTR1_NEW_VAL'].apply(pd.Series)], axis=1))