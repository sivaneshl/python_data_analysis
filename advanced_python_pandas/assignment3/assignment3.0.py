import pandas as pd
import numpy as np

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
                       usecols=[*range(2,6)],
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
merge1 = pd.merge(GDP, Energy, how='inner', left_on='Country Name', right_on='Country')
print(merge1)