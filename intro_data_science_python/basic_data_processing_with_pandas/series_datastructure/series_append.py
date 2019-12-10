import pandas as pd


# append - will not change the original series
original_sports = pd.Series({'Archery' : 'Bhutan',
                             'Golf' : 'Scotland',
                             'Sumo' : 'Japan',
                             'Taekwondo' : 'South Korea'})

cricket_loving_countries = pd.Series(['Australia',
                                      'Pakistan',
                                      'India'],
                                     index=['Cricket',
                                            'Cricket',
                                            'Cricket'])

all_countries = original_sports.append(cricket_loving_countries)
print(all_countries)
print(original_sports)
print(cricket_loving_countries)
