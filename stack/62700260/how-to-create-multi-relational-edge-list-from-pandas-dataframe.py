from itertools import *
import pandas as pd
import numpy as np

d = {'col1': ['a', 'b', 'c', 'd', 'a', 'b', 'd'], 'col2': ['XX', 'XX', 'XY', 'XX', 'YY', 'YY', 'XY']}
df_rel = pd.DataFrame(data=d)

uniq_nodes = df_rel['col1'].unique()

df1 = pd.DataFrame(data=list(combinations(uniq_nodes, 2)),  columns=['Src', 'Dst'])

newdf = pd.DataFrame(columns=['Src','Dst','Relationship'])
for i,  row in df1.iterrows():
    src = (df_rel[df_rel['col1'] == row['Src']]['col2']).to_list()
    dst = (df_rel[df_rel['col1'] == row['Dst']]['col2']).to_list()
    for x in src:
        if x in dst:
            newdf = newdf.append(pd.Series({'Src': row['Src'], 'Dst': row['Dst'], 'Relationship': x}),
                                 ignore_index=True, sort=False)

print(newdf)
