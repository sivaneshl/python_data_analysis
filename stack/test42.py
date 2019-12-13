import pandas as pd
import numpy as np

df = pd.DataFrame([['Hospital1', '2019-10-01'],
                   ['Hospital2', '2019-10-01'],
                   ['Hospital3', '2019-10-01'],
                   ['Hospital1', '2019-10-01'],
                   ['Hospital2', '2019-10-02'],
                   ['Hospital3', '2019-10-02'],
                   ['Hospital2', '2019-10-03'],
                   ['Hospital2', '2019-10-04'],
                   ['Hospital3', '2019-10-04'],
                   ['Hospital3', '2019-10-05'],
                   ['Hospital1', '2019-10-06'],
                   ['Hospital1', '2019-10-07'],
                   ['Hospital1', '2019-10-08']],
                  columns=['Hospital_Name', 'Date'])


df2 = pd.DataFrame([['Hospital1',12,15,16,12],
                    ['Hospital2',10,17,14,12],
                    ['Hospital2',15,20,12,12]],
                   columns=['Hospital_Name', '2019-10-01', '2019-10-02', '2019-10-03', '2019-10-04'])

print(pd.pivot_table(df, values='Date', index='Hospital_Name', aggfunc=np.size))

print(df2.sum())