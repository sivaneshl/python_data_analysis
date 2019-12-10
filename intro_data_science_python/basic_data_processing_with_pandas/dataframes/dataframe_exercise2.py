# Reindex the purchase records DataFrame to be indexed hierarchically, first by store, then by person.Name these indexes
# 'Location' and 'Name'.Then add a new entry to it with the value of:
# Name: 'Kevyn',
# Item Purchased: 'Kitty Food',
# Cost: 3.00
# Location: 'Store 2'.

import pandas as pd

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

df = df.set_index([df.index, 'Name'])
df.index.names=['Location','Name']
df=df.append(pd.Series(data={'Item Purchased': 'Kitty Food','Cost': 2.50},
                       name=('Store 2', 'Kevyn')))
print(df)


