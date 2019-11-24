import pandas as pd
import numpy as np

df = pd.read_csv('C:/python_data_analysis/resources/course1_downloads/cars.csv')
print(df.head())

# A pivot table allows us to pivot out one of these columns into a new column headers and compare it against another
# column as row indices.
# For instance, let's say we wanted to compare the makes of electric vehicles versus the years and that we wanted to do
# this comparison in terms of battery capacity
# To do this, we tell pandas we want the values to be kilowatts, the index to be the year and the columns to be the make.
print(pd.pivot_table(df, values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean))

# passing multiple functions to aggfunc
# and margins=True will give an All value
print(pd.pivot_table(df, values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean, np.min], margins=True))
