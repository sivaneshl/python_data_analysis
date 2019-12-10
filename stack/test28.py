import pandas as pd

df = pd.DataFrame([['1', '2011', 1],
                   ['1', '2012', 2],
                   ['1', '2013', 3],
                   ['2', '2011', 1],
                   ['2', '2012', 4],
                   ['2', '2013', 5],
                   ['3', '2011', 5],
                   ['3', '2012', 5],],
                  columns=['month','year','value']).set_index(['month','year'])

print(df)

print(df.index.get_level_values('month'))