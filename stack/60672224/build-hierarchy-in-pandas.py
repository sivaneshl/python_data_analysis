import pandas as pd
import numpy as np

df = pd.DataFrame({'e_id': [1,2,3,4,5,6],
                   's_id': [None,3,2,6,4,1]})

parents = dict(zip(df.e_id, df.s_id))
print(parents)

def find_child(x,i):
    if i==0:
        child_list.clear()
    child = parents.get(x)
    if child not in child_list:
        child_list.append(child)
    else:
        return child_list
    if pd.isnull(child)==False:
        find_child(child,1)
        return child_list


child_list = []
for idx, row in df.iterrows():
    print({row['e_id']:  find_child(row['e_id'], 0)})


