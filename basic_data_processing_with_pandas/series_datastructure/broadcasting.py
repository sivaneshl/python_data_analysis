import pandas as pd
import numpy as np


# broadcasting - apply an operation to every value in the series, changing the series.
# example = increase every random variable by 2, we could do so quickly using the += operator directly on the series object
s = pd.Series(np.random.randint(0,1000,10000))
s += 2
print(s.head())

# using the functional programming the same will be done as looping through the series and incrementing each valye
for label, value in s.iteritems():
    s.set_value(label, value+2)
print(s.head())


# add a new item to the series using iloc & loc
# if the value you pass in as the index doesnt exist then a new entry is added
a = pd.Series([1,2,3])
a.loc['Animal'] = 'Bear'
print(a)


