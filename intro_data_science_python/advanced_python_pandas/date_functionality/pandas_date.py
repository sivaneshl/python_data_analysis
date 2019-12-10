import pandas as pd
import numpy as np

# Timestamp
print(pd.Timestamp('9/1/2019 10:05AM'))

# Period
print(pd.Period('1/2019'))  # this is a period Jan 2019
print(pd.Period('3/5/2019'))    # period March 5th 2019

# DatetimeIndex
t1 = pd.Series(list('abc'), [pd.Timestamp('9/1/2019'), pd.Timestamp('9/2/2019'), pd.Timestamp('9/3/2019')])
print(t1)
print(type(t1))
print(type(t1.index))

# PeriodIndex
t2 = pd.Series(list('def'), [pd.Period('9/2019'),pd.Period('10/2019'), pd.Period('11/2019')])
print(t2)
print(type(t2))
print(type(t2.index))


# converting to datetime
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
# creating a random dataframe
t3 = pd.DataFrame(np.random.randint(0,100,(4,2)), index=d1, columns=list('ab'))
print(t3)  # the index date column is messy
t3.index = pd.to_datetime(t3.index)     # convet to datetime
print(t3)

# dayfirst
print(pd.to_datetime('4.7.12'))
print(pd.to_datetime('4.7.12', dayfirst=True))

# time deltas
print(pd.Timestamp('9/1/2019') - pd.Timestamp('2019-10-31'))
print(pd.Timestamp('9/1/2019') + pd.Timedelta('12D 3H'))

# working with dates in a dataframe
dates = pd.date_range('10/1/2016', freq='2W-SUN', periods=9)
print(dates)
df = pd.DataFrame({'Count1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                   'Count2': 120 + np.random.randint(-5, 10, 9)},
                  index=dates)
print(df)
# get the week day name
print(df.index.weekday_name)
# get diff between row values
print(df.diff())

# average of month
print(df.resample('M').mean())
# mean() for average
# 'M' for months

# partial indexing
print(df['2017'])
print(df['2016-10'])
print(df['2016-12':])   # Dec 2016 onwards
print(df['2016-10':'2016-12'])

# change the frequencey
# in this example change the frequency from biweekly to weekly
# and use ffill to fill the missing values
print(df.asfreq("W", method='ffill'))


