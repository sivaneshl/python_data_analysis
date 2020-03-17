import pandas as pd
from fuzzywuzzy.fuzz import partial_ratio
import difflib

df = pd.DataFrame([['a', 1, 'str1'],
                   ['a', 1, 'st2'],
                   ['a', 1, 'str3'],
                   ['a', 1, 'str10'],
                   ['a', 2, 'str4'],
                   ['a', 2, 'str5'],
                   ['a', 2, 'str6']],
                  columns=['product', 'city', 'value'])

def func(grp):
    def match(id, val):

        matches = grp.drop(id).apply(lambda x: difflib.SequenceMatcher(None, x['value'], val).ratio(), axis=1)
        return max([x for i, x in enumerate(matches) if x])

    return grp.apply(lambda row: match(row.name, row['value']), axis=1)


res = df.groupby(['product', 'city']).apply(func).reset_index()
res['level_2'] = df['value']
res.rename(columns={'level_2':'value'}, inplace=True)

print(res)