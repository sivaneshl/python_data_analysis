import pandas as pd

df = pd.read_csv('C:/python_data_analysis/resources/course1_downloads/olympics.csv',
                 index_col=0,
                 skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

# print(df.head())

names_ids = df.index.str.split('\s\(') # split the index by '('
# print(names_ids)

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
# print(df.head())


# question 0 - What is the first country in df?
print(df.iloc[0])

# question 1 - Which country has won the most gold medals in summer games?
print(df.nlargest(1, 'Gold').index.values[0])
# print(type(df.nlargest(1, 'Gold').index.values[0]))

# question 2 - Which country had the biggest difference between their summer and winter gold medal counts?
df['Gold_Diff'] = (df['Gold'] - df['Gold.1'])
print(df.nlargest(1, 'Gold_Diff').index.values[0])
# df=df.drop(['Gold_Diff'],axis=1)
# print(df.head())


# Question 3 - Which country has the biggest difference between their summer gold medal counts and winter gold medal counts
# relative to their total gold medal count? Only include countries that have won at least 1 gold in both summer and winter.
df['Gold_Diff_Rel'] = ((df['Gold'] - df['Gold.1']) / ((df['Gold'] + df['Gold.1'])))
has_gold = df[(df['Gold']>0) | (df['Gold.1']>0)]
print(has_gold.nlargest(10, 'Gold_Diff_Rel').index.values[0])


# Question 4 - Write a function that creates a Series called "Points" which is a weighted value where each gold medal
# (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The
# function should return only the column (a Series object) which you created, with the country names as indices.
df['Points'] = (df['Gold.2']*3)+(df['Silver.2']*2)+(df['Bronze.2']*1)
print(df.T.loc['Points'])