import numpy as np
import pandas as pd
from difflib import SequenceMatcher

def similar(dfg):
    df = pd.DataFrame(columns=['code', 'name'])

    if len(dfg) > 1:
        dfg = dfg.assign(a=1).merge(dfg[['name']].assign(a=1), on='a')
        dfg = dfg[dfg['name_x'] != dfg['name_y']]
        dfg[['name_x', 'name_y']] = pd.DataFrame(np.sort(dfg[['name_x', 'name_y']], axis=1), index=dfg.index)
        dfg = dfg.drop_duplicates(subset=['name_x', 'name_y'])
        dfg['sim'] = dfg.apply(lambda x: SequenceMatcher(None, x.name_x, x.name_y).ratio(), axis=1)

        for index, row in dfg.iterrows():
            if row['sim'] > 0:
                # this block could be more pythonic 
                row['name'] = row['name_x']
                df = df.append(row, sort=False)
                row['name'] = row['name_y']
                df = df.append(row, sort=False)
            else:
                row['name'] = row.name_x + ' + ' + row.name_y
                df = df.append(row, sort=False)
    else:
        df = df.append(dfg, sort=False)

    return df[['code', 'name']]

d = {'code': ['ABC', 'ABC', 'ABC', 'DB','DB','CDP'], 'name': ['abcde','abc de', 'xyz', 'defs','wokj','lkj']}
df = pd.DataFrame(data=d)
print(df)

df2 = df.groupby(['code']).apply(similar)
print(df2)
