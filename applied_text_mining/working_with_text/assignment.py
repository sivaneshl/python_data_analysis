# Assignment 1
# In this assignment, you'll be working with messy medical data and using regex to extract relevant infromation from
# the data.
# Each line of the dates.txt file corresponds to a medical note. Each note has a date that needs to be extracted,
# but each date is encoded in one of many formats.
# The goal of this assignment is to correctly identify all of the different date variants encoded in this dataset
# and to properly normalize and sort the dates.
#
# Here is a list of some of the variants you might encounter in this dataset:
#
# 04/20/2009; 04/20/09; 4/20/09; 4/3/09
# Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009;
# 20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009
# Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009
# Feb 2009; Sep 2009; Oct 2010
# 6/2008; 12/2009
# 2009; 2010
# Once you have extracted these date patterns from the text, the next step is to sort them in ascending chronological
# order accoring to the following rules:
#
# Assume all dates in xx/xx/xx format are mm/dd/yy
# Assume all dates where year is encoded in only two digits are years from the 1900's (e.g. 1/5/89 is January 5th, 1989)
# If the day is missing (e.g. 9/2009), assume it is the first day of the month (e.g. September 1, 2009).
# If the month is missing (e.g. 2010), assume it is the first of January of that year (e.g. January 1, 2010).
# Watch out for potential typos as this is a raw, real-life derived dataset.
# With these rules in mind, find the correct date in each note and return a pandas Series in chronological order of the
# original Series' indices.
#
# For example if the original series was this:
#
# 0    1999
# 1    2010
# 2    1978
# 3    2015
# 4    1985
# Your function should return this:
#
# 0    2
# 1    4
# 2    0
# 3    1
# 4    3
# Your score will be calculated using Kendall's tau, a correlation measure for ordinal data.
#
# This function should return a Series of length 500 and dtype int.

import pandas as pd
import numpy as np

pd.set_option('display.width', 400)
pd.set_option('display.max_rows', 600)

doc = []
with open('../resources/dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
# print(df.head(10))

dates = df.str.extractall(r'(?P<text>(?P<month>\d{1,2})[/-](?P<day>\d{1,2})[/-](?P<year>\d{2,4}))')
remaining_rows = ~df.index.isin([x[0] for x in dates.index])

dates = dates.append(df[remaining_rows].str.extractall(r'(?P<text>(?P<month>[a-zA-Z]{3,})\.?-? ?(?P<day>\d\d?)(th|nd|st)?,?-? ?(?P<year>\d{4}))'),sort=True)
# dates = dates.append(df[remaining_rows].str.extractall(r'(?P<text>(?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-. ]?)(?P<day>\d{1,2})(th|nd|st|rd)?[-, ]?(?P<year>\d{4}))'),sort=True)
remaining_rows = ~df.index.isin([x[0] for x in dates.index])
# print(dates)

dates = dates.append(df[remaining_rows].str.extractall(r'(?P<text>(?P<day>\d?\d) ?(?P<month>[a-zA-Z]{3,})\.?,? (?P<year>\d{4}))'),sort=True)
# dates = dates.append(df[remaining_rows].str.extractall(r'(?P<text>(?P<day>\d{1,2}) ?(?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[,. ]*)(?P<year>\d{4}))'),sort=True)
remaining_rows = ~df.index.isin([x[0] for x in dates.index])
# print(dates)

dates_without_day = df[remaining_rows].str.extractall(r'(?P<origin>(?P<month>[A-Z][a-z]{2,}),?\.? (?P<year>\d{4}))')
# dates_without_day = df[remaining_rows].str.extractall(r'(?P<text>(?P<month>(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[,. ]*)(?P<year>\d{4}))')
dates_without_day = dates_without_day.append(df[remaining_rows].str.extractall(r'(?P<text>(?P<month>\d{1,2})/(?P<year>\d{4}))'),sort=True)
dates_without_day['day'] = 1
dates = dates.append(dates_without_day, sort=True)
remaining_rows = ~df.index.isin([x[0] for x in dates.index])

dates_only_year = df[remaining_rows].str.extractall(r'(?P<text>(?P<year>\d{4}))')
dates_only_year['day'], dates_only_year['month'] = 1, 1
dates = dates.append(dates_only_year, sort=True)

dates = dates.reset_index()
# print(dates[dates['match']==1])
dates = dates[dates['match']==0]
dates.set_index('level_0', inplace=True)
# print(dates)

dates['year'] = dates['year'].apply(lambda x: '19' + str(x) if len(x) == 2 else str(x))

dates['month'] = dates['month'].apply(lambda x: x[1:] if type(x) is str and x.startswith('0') else x)
month_dict = dict({'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,
                   'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12,
                   'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9,
                   'Oct': 10, 'Nov': 11, 'Dec': 12, 'Since': 1, 'Age': 8, 'Janaury': 1, 'Decemeber': 12 })
dates['month'] = dates['month'].str.strip()
dates['month'] = dates['month'].str.strip(',')
dates['month'] = dates['month'].fillna('1')
dates.replace({'month': month_dict}, inplace=True)
dates['month'] = dates['month'].apply(lambda x: str(x))

dates['day'] = dates['day'].apply(lambda x: str(x))
print(dates.loc[225])

dates['date'] = dates['month'] + '/' + dates['day'] + '/' + dates['year']
dates['date'] = pd.to_datetime(dates['date'])
dates.sort_values(by='date', inplace=True)
print(dates[['date', 'month', 'day', 'year']])
print(pd.Series(list(dates.index)))




