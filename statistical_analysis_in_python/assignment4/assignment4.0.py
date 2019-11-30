import pandas as pd
import numpy as np
from scipy import stats
import re

pd.options.display.float_format = '{:.8f}'.format

# Definitions:
# # A quarter is a specific three month period,
#   Q1 is January through March,
#   Q2 is April through June,
#   Q3 is July through September,
#   Q4 is October through December.
# A recession is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive
# quarters of GDP growth.
# A recession bottom is the quarter within a recession which had the lowest GDP.
# A university town is a city which has a high percentage of university students compared to the total population of
# the city.

# Hypothesis: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the
# ratio of the mean price of houses in university towns the quarter before the recession starts compared to the
# recession bottom. (price_ratio=quarter_before_recession/recession_bottom)

# The following data files are available for this assignment:
# From the Zillow research data site there is housing data for the United States. In particular the datafile for all
# homes at a city level, City_Zhvi_AllHomes.csv, has median home sale prices at a fine grained level.
# From the Wikipedia page on college towns is a list of university towns in the United States which has been copy and
# pasted into the file university_towns.txt.
# From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States in current dollars
# (use the chained value in 2009 dollars), in quarterly intervals, in the file gdplev.xls. For this assignment, only
# look at GDP data from the first quarter of 2000 onward.

# Each function in this assignment below is worth 10%, with the exception of run_ttest(), which is worth 50%.

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National',
          'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana',
          'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho',
          'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan',
          'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico',
          'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa',
          'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana',
          'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California',
          'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island',
          'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia',
          'ND': 'North Dakota', 'VA': 'Virginia'}

quarterly_gdp = pd.read_excel('C:/python_data_analysis/resources/course1_downloads/gdplev.xls',
                              skiprows=219,
                              usecols=[4, 5, 6],
                              names=['Quarter', 'current_gdp', 'gdp'])


def get_list_of_university_towns():
    """Returns a DataFrame of towns and the states they are in from the
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
    columns=["State", "RegionName"]  )

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. """

    university_towns_df = pd.DataFrame(columns=['State', 'RegionName'])
    current_state = ''
    fhand = open('C:/python_data_analysis/resources/course1_downloads/university_towns.txt',
                 encoding='utf-8')
    for line in fhand:
        if line.endswith('[edit]\n'):
            current_state = line.replace('[edit]\n', '').strip()
        else:
            university_towns_df = university_towns_df.append({'State': current_state,
                                                              'RegionName': re.sub(r' \(.*\n', '', line).strip()},
                                                             ignore_index=True)
    # university_towns_df.replace(to_replace={'RegionName': r' \(.*\n'}, value={'RegionName': ''},
    #                             regex=True,
    #                             inplace=True)

    return university_towns_df


def get_recession_start():
    """Returns the year and quarter of the recession start time as a
    string value in a format such as 2005q3"""

    for i in range(0, len(quarterly_gdp['gdp'])-2):
        if quarterly_gdp.loc[i, 'gdp'] > quarterly_gdp.loc[i + 1, 'gdp'] > quarterly_gdp.loc[i + 2, 'gdp']:
            return quarterly_gdp.loc[i + 1, 'Quarter']


def get_recession_end():
    """Returns the year and quarter of the recession end time as a
    string value in a format such as 2005q3"""

    for i in range((quarterly_gdp[quarterly_gdp['Quarter'] == get_recession_start()].index.values[0]),
                   len(quarterly_gdp['gdp'])-2):
        if quarterly_gdp.loc[i, 'gdp'] < quarterly_gdp.loc[i + 1, 'gdp'] < quarterly_gdp.loc[i + 2, 'gdp']:
            return quarterly_gdp.loc[i + 1, 'Quarter']


def get_recession_bottom():
    """Returns the year and quarter of the recession bottom time as a
    string value in a format such as 2005q3"""

    recession_bottom_df = quarterly_gdp[quarterly_gdp['Quarter'] == get_recession_end()]
    recession_bottom_value = recession_bottom_df['gdp'].values[0]
    recession_bottom_index = recession_bottom_df.index.values[0]
    for i in range((quarterly_gdp[quarterly_gdp['Quarter'] == get_recession_start()].index.values[0]),
                   (quarterly_gdp[quarterly_gdp['Quarter'] == get_recession_end()].index.values[0])):
        if quarterly_gdp.loc[i, 'gdp'] < recession_bottom_value:
            recession_bottom_value = quarterly_gdp.loc[i, 'gdp']
            recession_bottom_index = i

    return quarterly_gdp.loc[recession_bottom_index, 'Quarter']


def convert_housing_data_to_quarters():
    """Converts the housing data to quarters and returns it as mean
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].

    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.

    The resulting dataframe should have 67 columns, and 10,730 rows.
    """
    # select desired columns
    columns_list = ['State', 'RegionName']
    year_month_list = [x for x in [None if i == 2016 and j > 8
                                   else str(i) + '-' + str(j).zfill(2)
                                   for i in range(2000, 2017)
                                   for j in range(1, 13)]
                       if x is not None]
    # this is a nested list comprehension where the inner list is to get all
    # the year and months and puts None for 2016-09/10/11/12 and the outer list
    # excludes the None values - Repalcement logic is below
    # for i in range(2000, 2017):
    #     for j in range(1, 13):
    #         if i == 2016 and j > 8:
    #             break
    #         else:
    #             column_name = str(i) + '-' + str(j).zfill(2)
    #             # if column_name in housing_df.columns:
    #             columns_list.append(column_name)

    columns_list = columns_list + year_month_list

    # Read data
    housing_df = pd.read_csv('C:/python_data_analysis/resources/course1_downloads/City_Zhvi_AllHomes.csv',
                             usecols=columns_list)

    # replace state codes from map
    housing_df['State'] = housing_df['State'].map(states)

    # reduce to quarters
    # find the quarters
    quarter_groups = dict()
    for yrmo in year_month_list:
        yearmonth = yrmo.split('-')
        quarter = int((int(yearmonth[1])-1)/3)+1
        quarter_groups.setdefault(yearmonth[0] + 'q' + str(quarter),[]).append(yrmo)

    # use the quarters and compute the mean
    columns_list = ['State', 'RegionName']
    for quarter, month_list in quarter_groups.items():
        housing_df[quarter] = housing_df[month_list].mean(axis=1)
        columns_list.append(quarter)

    # select the desired columns list and set State and RegionName as multi index
    housing_df = housing_df[columns_list].set_index(['State', 'RegionName'])
    return housing_df


get_list_of_university_towns()
# print(df[df['State'] == 'Massachusetts'])

recession_start = get_recession_start()
print('Recession Start', recession_start)
recession_end = get_recession_end()
print('Recession End', recession_end)
recession_bottom = get_recession_bottom()
print('Recession Bottom', recession_bottom)

convert_housing_data_to_quarters()

