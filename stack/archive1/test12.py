import pandas as pd
import numpy as np


df = pd.DataFrame([['app1', '01/01/2019'],
                   ['app2', '01/02/2019'],
                   ['app3', '01/02/2019'],
                   ['app4', '01/02/2019'],
                   ['app5', '01/04/2019'],
                   ['app6', '01/04/2019']],
                  columns=['app.no','date'])

print(pd.pivot_table(df, values='app.no', index='date', aggfunc=np.size))