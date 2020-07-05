import pandas as pd
import numpy as np

all_cases = pd.DataFrame([['123456','1/1/2019'],['789654','2/18/2019'],['852147','1/3/2018'],['93258','1/4/2019 ']],
                      columns=['EFE / Manual E-Form / Gate Pass No.','Realization Date'])
all_bca = pd.DataFrame([['123456','8/1/2019','88','8','8'],
                        ['789654','2/18/2019','300','30','10'],
                        ['852147','1/3/2018','500','25','20'],
                        ['93258','1/4/2019','1000','20','30'],
                        ['2530245','1/1/2019','333','33','33']],
                      columns=['EFE / Manual E-Form / Gate Pass No.','Realization Date','BCA(FC)','Charges','Commision'])

# solution1
# datadf['new_col'] = datadf.apply(lambda x: (np.where(x['country']+x['business'] == configdf['country']+configdf['business'])[0][0]),axis=1)
# datadf['new_col'] = datadf.apply(lambda x: (np.where((x['country'] == configdf['country']) & (x['business'] == configdf['business']))[0][0]),axis=1)
# print(datadf)
#
# # Solution2
# configdf.reset_index(inplace=True)
# print(configdf)
cross = all_cases.merge(all_bca,
                        on=['EFE / Manual E-Form / Gate Pass No.','Realization Date'],
                        how='right',
                        indicator='check')
print(cross)

