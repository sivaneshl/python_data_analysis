import pandas as pd
import numpy as np


df = pd.DataFrame([['2018-12-31',1603,'Pay Infringement',31/12/2018,'AustPost',209],
                   ['2018-12-31',1604,'Pay Infringement',31/12/2018,'AustPost',14],
                   ['2019-12-31',1605,'Pay Infringement',31/12/2018,'CSC',234],
                   ['2019-12-31',1606,'Pay Infringement',31/12/2018,'CSC',1],
                   ['2019-12-31',1607,'Pay Infringement',31/12/2018,'DTMR Other',1],
                   ['2018-12-31',1608,'Pay Infringement',31/12/2018,'Internet',496],
                   ['2018-12-30',1609,'Pay Infringement',30/12/2018,'CSC',266]],
                  columns=['ADATE','UoW','Category Description','Date','Channel','Trans'])
df = df.set_index(pd.to_datetime(df['ADATE']))
print(df)
grp = df['Trans'].groupby([df['Channel'],  df.index.year])
print(grp.transform('idxmin').dt.month, grp.transform('idxmax').dt.month)


