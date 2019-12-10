import pandas as pd
import numpy as np

# series is a combination of list and dictionary
# The items are all stored in an order and there's labels with which you can retrieve them. An easy way to visualize this is two columns of data
# documentation indicates that you can pass in some data, an index and a name. The data can be anything, that's array-like, like a list

animals = ['Tiger', 'Bear', 'Leapord']
animals_series = pd.Series(animals)
print(animals_series)
# pandas automatically identify the data type

numbers_series = pd.Series([1,2,3])
print(numbers_series)
# Underneath panda stores series values in a typed array using the Numpy library

print(pd.Series(['Tiger', 'Bear', None]))
# If we create a list of strings and we have one element, a None type, pandas inserts it as a None and uses the type
# object for the underlying array.
print(pd.Series([1, 2, None]))
# If we create a list of numbers, integers or floats, and put in the None type, pandas automatically converts this to a
# special floating point value designated as NAN, which stands for not a number.


# note that NaN is not None
print(np.nan == None)
print(np.nan == np.nan)
print(np.isnan(np.nan))


