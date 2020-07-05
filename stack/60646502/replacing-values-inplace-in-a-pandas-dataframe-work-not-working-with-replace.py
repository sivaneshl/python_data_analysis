import pandas as pd
import numpy as np

datax = pd.DataFrame([['A', 34.466667, 72.200000, 'B', np.NaN, np.NaN, np.NaN, np.NaN],
                      ['B', 33.766667, 72.366667, 'A', 'C', 'D', np.NaN, np.NaN],
                      ['C', 33.761500, 72.434000, 'B', 'E', 'G', np.NaN, np.NaN]],
                     columns=['Name', 'Latitude','Longitude','Link 1','Link 2','Link 3','Link 4','Link 5'])
# datax.set_index('Name', inplace=True)
# datax.fillna('', inplace=True)
print(datax)

for column in datax[['Link 1','Link 2','Link 3','Link 4','Link 5']]:
    datax['temp'] = datax[['Name', column]]\
        .fillna('').apply(sorted, axis=1)\
        .apply(lambda x: ','.join(map(str, x)))\
        .duplicated(keep='first')
    datax[column] = np.where(datax['temp']==True, np.NaN, datax[column])
    datax.drop('temp', axis=1, inplace=True)

print(datax)
# datax['L1'] = datax[['Name', 'Link 1']].apply(sorted, axis=1).apply(lambda x: ','.join(map(str, x))).duplicated(keep='first')
# datax['Link 1'] = np.where(datax['L1']==True, np.NaN, datax['Link 1'])
# print(datax.drop('L1', axis=1))
# print(datax.duplicated(subset=['L1'], keep='first'))