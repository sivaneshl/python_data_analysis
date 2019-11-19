import pandas as pd
import numpy as np


sports = {'Archery' : 'Bhutan',
          'Golf' : 'Scotland',
          'Sumo' : 'Japan',
          'Taekwondo' : 'South Korea'}
s = pd.Series(sports)
print(s)


# query by number - 4th country in the series
print(s.iloc[3])
# query by key - which country has 'Golf'
print(s.loc['Golf'])


# iterate through the series and do some operation
s = pd.Series([100.00, 120.00, 101.00, 3.00])
total = 0
for item in s:
    total+=item
print(total)
# this can be done faster by using vectorisation
# Pandas and the underlying NumPy libraries support a method of computation called vectorization.
# Vectorization works with most of the functions in the NumPy library, including the sum function.
total = np.sum(s)
print(total)


