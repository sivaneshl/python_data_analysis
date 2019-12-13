import io
import pandas as pd

# data = io.StringIO("""
# x y
# x y
#
# x y z a b c
# x y z a b c
# """)

df = pd.read_csv('test37.csv', delimiter='\t', skip_blank_lines=False)

df['emptyrow'] = df.isnull()
df['group'] = (df['emptyrow'] != df['emptyrow'].shift()).cumsum()
groups = df.groupby(by='group')

split_dfs = {}

for grp in groups.groups.keys():
    split_dfs[grp] = groups.get_group(grp).drop(['emptyrow','group'], axis=1)

print(split_dfs)