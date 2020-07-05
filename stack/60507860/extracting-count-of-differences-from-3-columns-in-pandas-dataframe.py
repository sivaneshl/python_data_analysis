import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

df = pd.DataFrame([['2020-02-27', 'google.com', 1000, 'good', 'naming_one'],
                   ['2020-02-27', 'google.com', 1000, 'good', 'naming_one'],
                   ['2020-02-27', 'google.com', 1000, 'good', 'naming_one'],
                   ['2020-02-27', 'google.com', 1002, 'bad', np.NaN],
                   ['2020-02-27', 'google.com', np.NaN, np.NaN, np.NaN],
                   ['2020-02-27', 'google.com', np.NaN, np.NaN, np.NaN],
                   ['2020-02-27', 'google.com', 1005, 'best','naming_two'],
                   ['2020-02-27', 'google.com', 1005, 'best','naming_two'],
                   ['2020-02-27', 'google.com', np.NaN, np.NaN, np.NaN],
                   ['2020-02-27', 'bing.com', 2000, 'good','naming_one'],
                   ['2020-02-27', 'bing.com', 2000, 'good', 'naming_one'],
                   ['2020-02-27', 'bing.com', 2004, 'bad', np.NaN],
                   ['2020-02-27', 'bing.com', np.NaN, np.NaN, np.NaN],
                   ['2020-02-27', 'yahoo.com', np.NaN, np.NaN, np.NaN],
                   ['2020-02-27', 'yahoo.com', 3000, 'best', 'naming_two'],
                   ['2020-02-27', 'yahoo.com', 3000, 'best', 'naming_two'],
                   ['2020-02-27', 'yahoo.com', np.NaN, np.NaN, np.NaN],
                   ['2020-02-27', 'yahoo.com', np.NaN, np.NaN, np.NaN],
                   ['2020-02-27', 'yahoo.com', 3006, 'best', 'naming_three'],
                   ['2020-02-27', 'yahoo.com', np.NaN, np.NaN, np.NaN],
                   ['2020-02-28', 'google.com', 1008, 'bad', 'naming_fifty'],
                   ['2020-02-28', 'google.com', 1010, 'good', 'naming_fifty'],
                   ['2020-02-28', 'google.com', 1009, 'worst', np.NaN],
                   ['2020-02-28', 'bing.com', 2010, 'good', 'naming_twenty'],
                   ['2020-02-28', 'yahoo.com', np.NaN, np.NaN, np.NaN],
                   ['2020-02-28', 'yahoo.com', 3009, 'worst', 'naming_eleven'],
                   ['2020-02-28', 'yahoo.com', np.NaN, np.NaN, np.NaN]],
                  columns=['Date','page','item_1','item_2','item_3'])

# print(df)
df.fillna(method='ffill',inplace=True)
df['new_item1'] = np.where(df['item_1']!=df['item_1'].shift(),1,0)
df['new_item2'] = np.where(df['item_2']!=df['item_2'].shift(),1,0)
df['new_item3'] = np.where(df['item_3']!=df['item_3'].shift(),1,0)

print(df)

grp = df.groupby(['Date','page'],as_index=False)['new_item1','new_item2','new_item3'].agg(sum)
print(grp.groupby('page').apply(lambda g: g.nlargest(1)))