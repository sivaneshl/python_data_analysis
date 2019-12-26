# An NOAA dataset has been stored in the file. The data for this assignment comes from a subset of The National Centers
# for Environmental Information (NCEI) Daily Global Historical Climatology Network (GHCN-Daily). The GHCN-Daily is
# comprised of daily climate records from thousands of land surface stations across the globe.
#
# Each row in the assignment datafile corresponds to a single observation.
#
# The following variables are provided to you:
#   id : station identification code
#   date : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
#   element : indicator of element type
#       TMAX : Maximum temperature (tenths of degrees C)
#       TMIN : Minimum temperature (tenths of degrees C)
#   value : data value for element (tenths of degrees C)
#
# For this assignment, you must:
#
# Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line
# graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between
# the record high and record low temperatures for each day should be shaded.
#
# Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record
# high or record low was broken in 2015.
#
# Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose
# of this visualization.
#
# Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider
# issues such as legends, labels, and chart junk.
#
# The data you have been given is near Ann Arbor, Michigan, United States, and the stations the data comes from are
# shown on the map below.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from calendar import month_abbr

# read the data csv file
df = pd.read_csv('fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
# print(df)

# convert to Celsius
df['Data_Value'] *= 1/10

# exclude Feb-29
df = df[~df['Date'].str.endswith(r'02-29')]
datetimeindex = pd.DatetimeIndex(df['Date'])
df['Year'], df['Month'], df['Day'] = datetimeindex.year, datetimeindex.month, datetimeindex.day

# exclude 2015
df_10year = df[df['Year'] != 2015]
df_2015 = df[df['Year'] == 2015]

# group ten year data by min and max of each day of the year
df_10year_min = df_10year[df_10year['Element'] == 'TMIN'].groupby(['Month', 'Day'], as_index=False).agg({'Data_Value':'min'})
df_10year_max = df_10year[df_10year['Element'] == 'TMAX'].groupby(['Month', 'Day'], as_index=False).agg({'Data_Value':'max'})

# group 2015 year data by min and max for each day of the year
df_2015_min = df_2015[df_2015['Element'] == 'TMIN'].groupby(['Month', 'Day'], as_index=False).agg({'Data_Value':'min'})
df_2015_max = df_2015[df_2015['Element'] == 'TMAX'].groupby(['Month', 'Day'], as_index=False).agg({'Data_Value':'max'})

# find outliers in 2015
outliers_2015_min = np.where(df_2015_min < df_10year_min)[0]
outliers_2015_max = np.where(df_2015_max > df_10year_max)[0]

plt.figure()
ax = plt.gca()

# create line graphs for max and min using 10 year data
plt.plot(df_10year_min['Data_Value'], color='green', alpha=0.5, label='Record High (2005-14)')
plt.plot(df_10year_max['Data_Value'], color='red', alpha=0.5, label='Record Low (2005-14)')
ax.fill_between(range(len(df_10year_min['Data_Value'])),
                       df_10year_min['Data_Value'], df_10year_max['Data_Value'],
                       facecolor='grey', alpha=0.5)

# create scatter graph using min and max of 2015 data
plt.scatter(x=outliers_2015_min, y=df_2015_min.iloc[outliers_2015_min]['Data_Value'],
            color='darkgreen', s=10, marker='o', label='Record Break - Low (2015)')
plt.scatter(x=outliers_2015_max, y=df_2015_max.iloc[outliers_2015_max]['Data_Value'],
            color='darkred', s=10, marker='o', label='Record Break - High (2015)')

print(outliers_2015_min)
print(df_2015_min.iloc[outliers_2015_min]['Data_Value'])


# legend
plt.legend(loc=8, frameon=False, fontsize=8)

# spines correction
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_facecolor('white')

# labels
plt.xlabel('Months of the year')
plt.ylabel('Temperature in Celsius')
plt.title('Ann Arbor, Michigan, United States \n 2005-2014 temperature trend and the 2015 record breaks')
# starting at 15 to make the labels in the middle
plt.xticks(np.linspace(15, 15+30*11, num=12),[s for s in month_abbr if s!=''])

plt.savefig('assignment2.png', format='png')
plt.show()






