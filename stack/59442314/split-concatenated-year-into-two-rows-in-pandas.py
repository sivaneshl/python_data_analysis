import pandas as pd
import numpy as np
from pandas import Series

df = pd.DataFrame({'Year': ['2008-09','2008-09','2008-09','2008-09','2008-09'],
                   'Province': ['Federal','Federal','Federal','Federal','Federal'],
                   'Grade': [22,21,20,19,18],
                   'Male': [100,324,820,2159,4824],
                   'Female': [6,19,90,389,869],
                   'Unnamed': [np.NaN,np.NaN,np.NaN,np.NaN,np.NaN]})

# df['Year'] = [x.split('-') for x in df['Year'].tolist()]

# df.assign(var1=df.var1.str.split(',')).explode('var1').reset_index(drop=True)

print(df.assign(Year=df.Year.str.split('-')).explode('Year').reset_index(drop=True))