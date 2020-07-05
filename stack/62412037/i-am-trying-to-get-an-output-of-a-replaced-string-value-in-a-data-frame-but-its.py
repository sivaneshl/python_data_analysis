import pandas as pd

df = pd.DataFrame(['China, Hong Kong Special Administrative Region',
                   'United Kingdom of Great Britain and Northern Ireland',
                   'Republic Of Korea',
                   'United States of America',
                   'Iran (Islamic Republic of)'],
                  columns=['Country'])
print(df)

df['Country'] = df['Country'].replace({'China, Hong Kong Special Administrative Region': 'Hong Kong',
                                       'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
                                       'Republic Of Korea': 'South Korea',
                                       'United States of America': 'United States',
                                       'Iran (Islamic Republic of)': 'Iran'})
print(df)