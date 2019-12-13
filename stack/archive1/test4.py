import pandas as pd
import numpy as np

country = pd.DataFrame([['country1','city1','zip1'],['country1','city1','zip2'],['country1','city2','zip3'],['country1','city2','zip4'],
                       ['country2','city3','zip5'],['country2','city3','zip6'],['country2','city4','zip7'],
                       ['country3','city5','zip8'],['country3','city6','zip9']],
                      columns=['country','city','zipcode'])
continent = pd.DataFrame([['country1','A'],['country2','B'],['country3','C'],['country4','D'],['country5','E']],
                      columns=['country','continent'])

# solution1
# datadf['new_col'] = datadf.apply(lambda x: (np.where(x['country']+x['business'] == configdf['country']+configdf['business'])[0][0]),axis=1)
# datadf['new_col'] = datadf.apply(lambda x: (np.where((x['country'] == configdf['country']) & (x['business'] == configdf['business']))[0][0]),axis=1)
# print(datadf)
country['continent'] = country.apply(lambda x: (np.where(x['country'] == continent['country'])[0][0]),axis=1)
print(country)

# Solution2
# country = (country.merge(continent, on=['country']))
# print(country)

