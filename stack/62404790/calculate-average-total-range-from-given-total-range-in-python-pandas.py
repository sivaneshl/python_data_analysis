import pandas as pd
import numpy as np
#
# df = pd.DataFrame([['FUTIDX','BANKNIFTY','6/1/2020',729.8],
#                    ['FUTIDX','BANKNIFTY','6/2/2020',834],
#                    ['FUTIDX','BANKNIFTY','6/3/2020',1145.2],
#                    ['FUTIDX','BANKNIFTY','6/4/2020',846.7],
#                    ['FUTIDX','BANKNIFTY','6/5/2020',812.5],
#                    ['FUTIDX','BANKNIFTY','6/8/2020',904.6],
#                    ['FUTIDX','BANKNIFTY','6/9/2020',1014],
#                    ['FUTIDX','BANKNIFTY','6/10/2020',660],
#                    ['FUTIDX','BANKNIFTY','6/11/2020',796],
#                    ['FUTIDX','BANKNIFTY','6/12/2020',1173],
#                    ['FUTIDX','BANKNIFTY','6/15/2020',969],
#                    ['FUTIDX','BANKNIFTY','6/16/2020',271],
#                    ['FUTIDX','NIFTY','6/1/2020',207],
#                    ['FUTIDX','NIFTY','6/2/2020',230],
#                    ['FUTIDX','NIFTY','6/3/2020',177.7]],
#                   columns=['INSTRUMENTS','SYMBOL','TIMESTAMP','TR'])


df = pd.DataFrame([['FUTIDX','BANKNIFTY','6/1/2020',10],
                   ['FUTIDX','BANKNIFTY','6/2/2020',20],
                   ['FUTIDX','BANKNIFTY','6/3/2020',30],
                   ['FUTIDX','BANKNIFTY','6/4/2020',40],
                   ['FUTIDX','BANKNIFTY','6/5/2020',50],
                   ['FUTIDX','BANKNIFTY','6/8/2020',10],
                   ['FUTIDX','BANKNIFTY','6/9/2020',20],
                   ['FUTIDX','BANKNIFTY','6/10/2020',30],
                   ['FUTIDX','BANKNIFTY','6/11/2020',40],
                   ['FUTIDX','BANKNIFTY','6/12/2020',50],
                   ['FUTIDX','BANKNIFTY','6/15/2020',10],
                   ['FUTIDX','BANKNIFTY','6/16/2020',20],
                   ['FUTIDX','NIFTY','6/1/2020',10],
                   ['FUTIDX','NIFTY','6/2/2020',20],
                   ['FUTIDX','NIFTY','6/3/2020',30]],
                  columns=['INSTRUMENTS','SYMBOL','TIMESTAMP','TR'])


df['Av.TR'] = df.groupby('SYMBOL')['TR'].transform(lambda x: x.rolling(5).mean())
print(df)

for key, grp in df.groupby('SYMBOL'):
    print(grp, type(grp))
    for i, row in grp.iterrows():
        grp.set_value(i, 'Av.TR', np.where(grp.shift(1)['Av.TR'].isna(), np.NaN, (grp.shift(1)['Av.TR'] * 4 + row['TR']) / 5))

print(df)
# df['new_col'] = df.apply(lambda x: (np.where((x['text_original'] == df1['text_original']) or (x['text_original'] == df1['text_compare']))[0][0]),axis=1)
