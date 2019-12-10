# The DataFrame is conceptually a two-dimensional series object, where there's an index and multiple columns of content,
# with each column having a label. In fact, the distinction between a column and a row is really only a conceptual
# distinction. And you can think of the DataFrame itself as simply a two-axes labeled array.

# You can create a DataFrame in many different ways, some of which you might expect. For instance, you can use a group
# of series, where each series represents a row of data. Or you could use a group of dictionaries, where each dictionary
# represents a row of data.

import pandas as pd


# 3 purchase order records as serires object
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased' : 'Dog Food',
                        'Cost' : 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
print(df)

# query using loc
# if single result then the result will be a series
print(df.loc['Store 2'])
print(type(df.loc['Store 2']))
# if multiple rows are returned then the result will be a dataframe
print(df.loc['Store 1'])
print(type(df.loc['Store 1']))

# get all values from a column
print(df['Item Purchased'])

# get a  cell value by passing row index and column index to loc
print(df.loc['Store 1', 'Cost'])
# get multiple columns for a row
print(df.loc['Store 1', ['Item Purchased', 'Cost']])

# to get the column values - we can transpose the df and query using loc and iloc
print(df.T.loc['Item Purchased'])

# chaining
print(df.loc['Store 1']['Cost'])
print(df.loc[:, ['Name', 'Cost']])


# drop a row using row label or index
df.drop('Store 2')
# drop does not change the dataframe instead it returns a view of the dataframe with the rows dropped
print(df)
# the original dataframe remains unchanged
copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
print(copy_df)

# drop and update - using inplace
copy_df = df.copy()
copy_df.drop( 'Store 1', inplace = True)
print(copy_df)

# drop a column - using axis
# axis is default 0 indicating row
# set axis = 1 indicating column
copy_df = df.copy()
copy_df=copy_df.drop( 'Cost', axis=1)
print(copy_df)

# remove a column using del - this will update the df unlike drop
copy_df = df.copy()
del copy_df['Name']
print(copy_df)


# add a new column
df['Location'] = None
print(df)

# using broadcast to discount 20% in cost
df['Cost'] -= df['Cost']*.2
print(df)







