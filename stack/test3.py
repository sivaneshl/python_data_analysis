import pandas as pd
import numpy as np

datadf = pd.DataFrame([['A','1'],['A','1'],['A','2'],['A','2'],['B','1'],['B','1'],['B','2'],['C','1'],['C','2']],
                      columns=['country','business'])
configdf = pd.DataFrame([['A','1'],['A','2'],['B','1'],['B','2'],['C','1'],['C','2']],
                      columns=['country','business'])

# solution1
# datadf['new_col'] = datadf.apply(lambda x: (np.where(x['country']+x['business'] == configdf['country']+configdf['business'])[0][0]),axis=1)
# datadf['new_col'] = datadf.apply(lambda x: (np.where((x['country'] == configdf['country']) & (x['business'] == configdf['business']))[0][0]),axis=1)
# print(datadf)
#
# # Solution2
configdf.reset_index(inplace=True)
print(configdf)
newdf = datadf.merge(configdf, on=['country', 'business'])
print(newdf)

