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


# set_index function - to set the index for a df
# takes a list of columns and promotes them as index
# example - index using number of gold instead of country
# we need to preserve the country information into a new column
# We can do this using the indexing operator or the string that has the column label.
# Then we can use the set_index to set index of the column to summer gold medal wins.
df['Country']=df.index
df = df.set_index('Gold')
print(df.head())


# We can get rid of the index completely by calling the function reset_index. This promotes the index into a column and
# creates a default numbered index.
df = df.reset_index()
print(df.head())

# multi level index
census_df = pd.read_csv("C:/python_data_analysis/resources/course1_downloads/census.csv")
print(census_df.head())

# get unique values from a column
print(census_df['SUMLEV'].unique())


# reduce the df to only summary level at county level
census_df = census_df[census_df['SUMLEV']==50]
print(census_df.head())


# reduce the data that we're going to look at to just the total population estimates and the total number of births
# We can do this by creating a list of column names that we want to keep then project those and assign the resulting
# DataFrame to our df variable.
columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
census_df = census_df[columns_to_keep]
print(census_df.head())

# set  multiple index
census_df = census_df.set_index(['STNAME','CTYNAME'])
print(census_df.head())

# querying
print(census_df.loc['Michigan'])
# querying using multi index - using the loc method
print(census_df.loc['Michigan','Wayne County'])
# we need to provide two values as each element of our filtering list
print(census_df.loc[[('Michigan','Wayne County'),('Michigan','Ottawa County')]])
