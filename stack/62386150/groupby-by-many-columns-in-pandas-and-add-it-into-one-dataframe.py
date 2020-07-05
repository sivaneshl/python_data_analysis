import pandas as pd

df = pd.DataFrame([[10, 1, 0, 1],
                   [20, 0, 1, 1],
                   [30, 1, 1, 0],
                   [40, 0, 0, 1],
                   [50, 1, 1, 0]],
                  columns=['usd','java','python','c'])

print(df)

df2 = pd.DataFrame()

for lang in df.columns[1:]:
    group_lang = (df.groupby(lang)['usd'].mean().reset_index())
    group_lang['lang'] = lang
    df2 = pd.concat([df2, group_lang[['lang','usd']]])

df2=df2.reset_index().set_index('lang').rename(columns={'index':'val'})
print(df2)

