import numpy as np
import pandas as pd
df = pd.DataFrame([['A', 'one',  105], ['A', 'two',  101], ['A', 'three',  103],
                      ['B','one',  101], ['B','two',  1102], ['B','three',  1050]],
                   columns=['c1', 'c2', 'c3'])
df = df.set_index(['c1', 'c2'])
print(df)

# print(df.sort_values(['c1','c3'], ascending=False).groupby('c3'))
# grp = df.groupby(['c1', 'c2'])
# print(grp[['c3']].transform(sum).sort_values('c3'))

print(df.sort_values(['c1','c3'], ascending=False).groupby(['c1','c3']).agg(lambda x: x))