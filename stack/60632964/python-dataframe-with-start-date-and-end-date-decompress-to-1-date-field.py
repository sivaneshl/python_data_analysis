import pandas as pd

df = pd.DataFrame([['2019-01-15','2019-01-31','A',121.0],
                   ['2019-02-01','2020-03-10','A',136.0],
                   ['2006-10-02','2020-03-10','B',136.0],
                   ['2003-07-31','2020-03-10','B',321.0],
                   ['2010-11-03','2020-03-10','C',322.0],
                   ['2013-02-01','2017-02-07','D',375.0],
                   ['2017-02-08','2019-01-14','D',375.0],
                   ['2019-01-15','2019-04-29','D',375.0],
                   ['2019-04-30','2020-03-10','D',375.0]],
                  columns=['StartDate','EndDate','Company','Location'])
df['StartDate'] = pd.to_datetime(df['StartDate'])
df['EndDate'] = pd.to_datetime(df['EndDate'])
df.set_index('Company', inplace=True)
df['row'] = range(len(df))
print(df)

starts = df[['StartDate', 'Location', 'row']].rename(columns={'StartDate': 'Date'})
ends = df[['EndDate', 'Location', 'row']].rename(columns={'EndDate':'Date'})
df_decomp = pd.concat([starts, ends])
df_decomp = df_decomp.set_index('row', append=True)
df_decomp.sort_index()
print(df_decomp)

df_decomp = df_decomp.groupby(level=[0,1]).apply(lambda x: x.set_index('Date').resample('D').fillna(method='pad'))
df_decomp = df_decomp.reset_index(level=1, drop=True)
print(df_decomp.loc['D'])



