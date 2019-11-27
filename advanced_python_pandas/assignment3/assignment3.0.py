import pandas as pd
import numpy as np

pd.options.display.float_format = '{:.8f}'.format

# Question 1 #

# Load the energy data from the file Energy Indicators.xls, which is a list of indicators of energy supply and renewable
# electricity production from the United Nations for the year 2013, and should be put into a DataFrame with the variable
# name of energy.

# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer
# and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and
# you should change the column labels so that the columns are:
# # ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

Energy = pd.read_excel('C:/python_data_analysis/resources/course1_downloads/Energy Indicators.xls',
                       # skip header rows - header rows are till 18, 19th row is the actual data start
                       skiprows=18,
                       # skip footer - last 38 rows are not needed
                       skipfooter=38,
                       # cols 1 & 2 are blank - so ignore them and use only cols 2-5 (passed as a list)
                       usecols=[*range(2, 6)],
                       # rename the columns
                       names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])

# Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule).
Energy['Energy Supply'] *= 1000000

# For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.
Energy.replace(regex=r'[.]+', value=np.NaN, inplace=True)

# There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these,
# e.g.
# 'Bolivia (Plurinational State of)' should be 'Bolivia',
Energy.replace(to_replace={'Country': r'\(.*\)'}, value={'Country': ''}, regex=True, inplace=True)
# using replace function with column name and regex for paranthesis
# 'Switzerland17' should be 'Switzerland'
Energy.replace({'Country': r'[0-9]'}, {'Country': ''}, regex=True, inplace=True)
# here using replace function with column name; to_replace and value are implicit
Energy['Country'] = Energy['Country'].str.strip()
# strip off extra spaces

# Rename the following list of countries (for use in later questions):
# "Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"
Energy.replace({"Republic of Korea": "South Korea",
                "United States of America": "United States",
                "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                "China, Hong Kong Special Administrative Region": "Hong Kong"},
               inplace=True)

# print(Energy)

# Next, load the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from
# World Bank. Call this DataFrame GDP.
#
# Make sure to skip the header, and rename the following list of countries:
# "Korea, Rep.": "South Korea",
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"
GDP = pd.read_csv('C:/python_data_analysis/resources/course1_downloads/world_bank.csv',
                  skiprows=4)
GDP.replace({"Korea, Rep.": "South Korea",
             "Iran, Islamic Rep.": "Iran",
             "Hong Kong SAR, China": "Hong Kong"},
            inplace=True)

# print(GDP)

# Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file
# scimagojr-3.xlsx, which ranks countries based on their journal contributions in the aforementioned area.
# Call this DataFrame ScimEn.
ScimEn = pd.read_excel('C:/python_data_analysis/resources/course1_downloads/scimagojr-3.xlsx')

# print(ScimEn)

# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names).
# Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).
# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents',
# 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy
# Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
# This function should return a DataFrame with 20 columns and 15 entries.
column_list = ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
               'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable',
               '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
intersection_df = (Energy.merge(GDP, how='inner', left_on='Country', right_on='Country Name')
                   .merge(ScimEn, how='inner', on='Country'))
intersection_df.index = intersection_df['Country']
Top15 = intersection_df.nsmallest(15, 'Rank')[column_list]
print(Top15)

# Just compare the countries and get the intersection
# Energy_Country = set(Energy.set_index('Country').index.values)
# GDP_Country = set(GDP.set_index('Country Name').index.values)
# ScimEn_Country = set(ScimEn.set_index('Country').index.values)
# print(Energy_Country.__len__())
# print(GDP_Country.__len__())
# print(ScimEn_Country.__len__())
# print(Energy_Country.intersection(GDP_Country).intersection(ScimEn_Country).__len__())
# print(Energy_Country.union(GDP_Country).union(ScimEn_Country).__len__())





# Question 2 #
# The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the
# datasets, but before you reduced this to the top 15 items, how many entries did you lose?
# This function should return a single number.
Energy.index = Energy['Country']
GDP.index = GDP['Country Name']
ScimEn.index = ScimEn['Country']
intersection_df = (Energy.merge(GDP, how='inner', left_index=True, right_index=True)
                   .merge(ScimEn, how='inner', left_index=True, right_index=True))
union_df = (Energy.merge(GDP, how='outer', left_index=True, right_index=True)
            .merge(ScimEn, how='outer', left_index=True, right_index=True))
print(len(union_df) - len(intersection_df))


# Question 3 #
# What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
# This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.
GDP_columns = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
avgGDP = Top15[GDP_columns].mean(axis=1).sort_values(ascending=False)
print(avgGDP)


# Question 4 #
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# This function should return a single number.
sixth_gdp_country = avgGDP.index[5]
print(Top15.loc[sixth_gdp_country,'2015'] - Top15.loc[sixth_gdp_country,'2006'])


# Question 5 #
# What is the mean Energy Supply per Capita?
# This function should return a single number.
print(np.mean(Top15['Energy Supply per Capita']))
# print(Top15['Energy Supply per Capita'].mean())


# Question 6 #
# What country has the maximum % Renewable and what is the percentage?
# This function should return a tuple with the name of the country and the percentage.
max_renewable_tuple = (tuple((Top15['% Renewable'].idxmax(), Top15['% Renewable'].max())))
print(max_renewable_tuple)
# the following also can be used
# max_renewable = Top15.nlargest(1, '% Renewable')['% Renewable']
# print(tuple(zip(max_renewable.index, max_renewable)))


# Question 7 #
# Create a new column that is the ratio of Self-Citations to Total Citations. What is the maximum value for this new
# column, and what country has the highest ratio?
# This function should return a tuple with the name of the country and the ratio.
from fractions import Fraction
Top15['Citation Ratio'] = [str(Fraction(x, y)).replace('/', ':')
                             for x, y in zip(Top15['Self-citations'], Top15['Citations'])]
Top15['Citation Temp'] = Top15['Self-citations'] / Top15['Citations']
# print(Top15[['Self-citations', 'Citations', 'Citation Ratio', 'Citation Temp']])
print(tuple((Top15['Citation Temp'].idxmax(), Top15['Citation Temp'].max())))
Top15 = Top15.drop('Citation Temp', axis=1)


# Question 8 #
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. What is the third most
# populous country according to this estimate?
# This function should return a single string value.
Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
# print(Top15[['Energy Supply', 'Energy Supply per Capita', 'Population']])
print(Top15.nlargest(3,'Population').index[-1])


# Question 9 #
# Create a column that estimates the number of citable documents per person. What is the correlation between the number
# of citable documents per capita and the energy supply per capita? Use the .corr() method, (Pearson's correlation).
# This function should return a single number.
# (Optional: Use the built-in function plot9() to visualize the relationship between Energy Supply per Capita vs.
# Citable docs per Capita)
Top15['citable documents per person']=Top15['Citable documents']/Top15['Population']
print(Top15['citable documents per person'].corr(Top15['Energy Supply per Capita']))


# Question 10 #
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the
# top 15, and a 0 if the country's % Renewable value is below the median.
# This function should return a series named HighRenew whose index is the country name sorted in ascending order of rank.
median_renewable = Top15['% Renewable'].median()
print(median_renewable)
Top15['HighRenew'] = (Top15['% Renewable'] >= median_renewable).astype(int)
print(Top15.sort_values(by='Rank', ascending=True)[['% Renewable','HighRenew']])


# Question 11 (6.6%)
# Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample
# size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated
# population of each country.
# ContinentDict  = {'China':'Asia',
#                   'United States':'North America',
#                   'Japan':'Asia',
#                   'United Kingdom':'Europe',
#                   'Russian Federation':'Europe',
#                   'Canada':'North America',
#                   'Germany':'Europe',
#                   'India':'Asia',
#                   'France':'Europe',
#                   'South Korea':'Asia',
#                   'Italy':'Europe',
#                   'Spain':'Europe',
#                   'Iran':'Asia',
#                   'Australia':'Australia',
#                   'Brazil':'South America'}
# This function should return a DataFrame with index named Continent
# ['Asia', 'Australia', 'Europe', 'North America', 'South America'] and columns ['size', 'sum', 'mean', 'std']
ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}
Top15['Continent'] = Top15.index.to_series().map(ContinentDict)
print(Top15.groupby('Continent')['Population']
      .agg([('size', np.size), ('sum', np.sum), ('mean', np.mean), ('std', np.std)]))


# Question 12 #
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries 
# are in each of these groups?
# This function should return a Series with a MultiIndex of Continent, then the bins for % Renewable. Do not include 
# groups with no countries.
result_12 = (Top15.groupby(['Continent', pd.cut(Top15['% Renewable'], 5)]).size().dropna())
print(result_12)
print(type(result_12))





# Question 13 #
# Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
# # e.g. 317615384.61538464 -> 317,615,384.61538464
# This function should return a Series PopEst whose index is the country name and whose values are the population estimate string.
PopEst = Top15['Population'].apply(lambda x : "{:,}".format(x))
print(PopEst)





