import pandas as pd


# series can be created from dictionary data
# the index is automatically assigned to the keys of the dictionary
sports = {'Archery' : 'Bhutan',
          'Golf' : 'Scotland',
          'Sumo' : 'Japan',
          'Taekwondo' : 'South Korea'}
s = pd.Series(sports)
print(s)
# panda set the data type of the series to object
# countries as the value of the series and that the index values can be set to the keys from our dictionary
print(s.index)
print(s.values)

# You could also separate your index creation from the data by passing in the index as a list explicitly to the series
s = pd.Series(['Tiger', 'Bear', 'Monkey'], index=['India', 'America', 'Canada'])
print(s)
# index and dict values separately
s = pd.Series(sports, index=['Golf', 'Sumo', 'Archery', 'Taekwondo'])
print(s)
# index items not matching the dict keys
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
print(s)

