import pandas as pd

df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                  index=['Store 1', 'Store 1', 'Store 2'])
print(df)

# add new columns
df['Date'] = ['December 1', 'January 1', 'mid-May']
df['Delivered'] = True
print(df)

# adding new column value to only some rows
df['Feedback'] = ['Positive', None, 'Negative']
print(df)

# adding new column value to only some rows by using the default index
adf = df.reset_index()
adf['Date'] = pd.Series({0:'December 1',2:'mid-May'})
print(adf)