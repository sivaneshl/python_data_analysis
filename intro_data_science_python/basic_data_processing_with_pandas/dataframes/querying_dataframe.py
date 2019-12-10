import pandas as pd


df = pd.read_csv("C:/python_data_analysis/resources/course1_downloads/olympics.csv",
                 index_col=0,
                 skiprows=1)
for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col:'#'+col[2:]}, inplace=True)

# creating a boolean mask - a boolean mask is a series (1D) or data frame (2D) where the values are either True or False
# we can create a boolean mask for a data frame for the list of countries that have a Gold
print(df['Gold'] > 0)

# overlay that mask on the data frame -  using the where function
# The where function takes a Boolean mask as a condition, applies it to the data frame or series, and returns a new
# data frame or series of the same shape
# Apply this Boolean mask to our Olympics data and create a data frame of only those countries who have won a gold at a
# summer games
only_gold = df.where(df['Gold'] > 0)
print(only_gold.head())
# We see that the resulting data frame keeps the original indexed values, and only data from countries that met the
# condition are retained. All of the countries which did not meet the condition have NaN data instead. This is okay.
# Most statistical functions built into the data frame object ignore values of NaN.
# For instance, if we call the df.count on the only gold data frame, we see that there are 100 countries which have had
# gold medals awarded at the summer games, while if we call count on the original data frame, we see that there are 147
# countries total.
print(only_gold['Gold'].count(), df['Gold'].count())

# if we want to drop the rows with NaN use drop function
# default axis is rows (0); to drop by columns uss axis=1
only_gold = only_gold.dropna()
print(only_gold.head())

# without using the where function we can directly pass the boolean mask to the dataframe and get non NaN rows
only_gold = df[df['Gold']>0]
print(only_gold.head())

# countries that won gold in either summer or winter olympics
both_gold = df[(df['Gold']>0) | (df['Gold.1']>0)]
print(both_gold.head())
print(len(both_gold))

only_winter_gold = df[(df['Gold.1']>0) & (df['Gold']==0)]
print(only_winter_gold.head())
print(len(only_winter_gold))


