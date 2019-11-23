import pandas as pd

census_df = pd.read_csv('C:/python_data_analysis/resources/course1_downloads/census.csv')
# print(census_df.head())


# Question 5 - Which state has the most counties in it?
# reduce the df to county level (SUMLEV==50) with only STATE and COUNTY columns
# and groupby STATE and count - this will result in a df
# now find the largest row in the df and extract the index value (STATE)
state_with_most_county = census_df[census_df['SUMLEV']==50][['STATE','COUNTY']]\
    .groupby(['STATE']).count()\
    .nlargest(1,'COUNTY').index.values[0]
# print(state_with_most_county)
# reduce the main df with only states and get the State name
# state_df = census_df[census_df['SUMLEV']==40][['STATE','STNAME']].set_index('STATE')
print(census_df[census_df['SUMLEV']==40][['STATE','STNAME']].set_index('STATE').loc[state_with_most_county].values[0])


# Question 6 - Only looking at the three most populous counties for each state, what are the three most populous states
# (in order of highest population to lowest population)? This function should return a list of string values.
populous_states_ids = census_df[census_df['SUMLEV']==50][['STATE','COUNTY','CENSUS2010POP']]\
    .groupby(['STATE'])\
    .apply(lambda x: x.nlargest(3,'CENSUS2010POP'))\
    .sum(level='STATE')\
    .nlargest(3, ['CENSUS2010POP'])\
    .index.values
populous_states_list=[]
for st in populous_states_ids:
    populous_states_list.append(census_df[census_df['SUMLEV'] == 40][['STATE', 'STNAME']].set_index('STATE').loc[st].values[0])
print(populous_states_list)


# Question 7 - Which county has had the largest absolute change in population within the period 2010-2015?
# (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
# This function should return a single string value.
colunms_list = ['STATE','COUNTY','POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
largest_change_df = census_df[census_df['SUMLEV']==50][colunms_list]
largest_change_df['min'] = largest_change_df[colunms_list[2:]].min(axis=1)
largest_change_df['max'] = largest_change_df[colunms_list[2:]].max(axis=1)
largest_change_df['change'] = largest_change_df['max'] - largest_change_df['min']
county_idx=largest_change_df.nlargest(3,'change').index.values[0]
print(census_df.loc[county_idx,'CTYNAME'])
# print(county_idx)


# Question 8 - In this datafile, the United States is broken up into four regions using the "REGION" column
# Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose
# POPESTIMATE2015 was greater than their POPESTIMATE2014. This function should return a 5x2 DataFrame with the columns
# = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index)
reduced_df = census_df[(census_df['SUMLEV']==50) &
                       ((census_df['REGION']==1) | (census_df['REGION']==2)) &
                       (census_df['CTYNAME'].str.startswith('Washington')) &
                       (census_df['POPESTIMATE2015']>census_df['POPESTIMATE2014'])][['STNAME', 'CTYNAME']]
print(reduced_df)