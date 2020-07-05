import pandas as pd

df = pd.DataFrame({'A': ('foo', 'foo', 'foo', 'foo', 'foo'),
                   'start': (3039, 3536, 9140, 12976, 14982),
                   'end': (3536, 4879, 44331, 13641, 15643)})
df2=df
groups=pd.Series([1]*len(df))
while (groups.value_counts()>1).any():
    groups=( df2['start'].gt(df2['start'].shift())  & df2['end'].gt(df2['end'].shift()) ).cumsum()
    print(groups)
    df2=df2.groupby(groups,as_index=False).first()

print(df2)