import pandas as pd

obj1 = pd.DataFrame([['Monday',1,2,3],
                     ['Tuesday',4,5,6]],
                    columns=['dayofweek','A','B','C'])
obj2 = pd.DataFrame([['Monday',2,1,3],
                     ['Tuesday',5,4,6]],
                    columns=['dayofweek','A','B','C'])
obj3 = pd.DataFrame([['Monday',3,2,1],
                     ['Tuesday',6,5,4]],
                    columns=['dayofweek','A','B','C'])
obj1=obj1.set_index('dayofweek')
obj2=obj2.set_index('dayofweek')
obj3=obj3.set_index('dayofweek')
df = pd.concat([obj1, obj2, obj3], keys=('Obj1', 'Obj2', 'Obj3'), axis=1)
print(df)