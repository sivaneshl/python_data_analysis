import pandas as pd

b = pd.DataFrame({'col1':['a','a','b','b','c','d'], 'col2':['b','b','a','a','d','c']})
print(b)


# b['col3'] = list(zip(b['col1'],b['col2']))
# b['col3'] =
print(b.groupby((b['col1'] + '-' + b['col2'])).size())

#
# print(
#     b.groupby([['col1','col2']], axis=1).count().reset_index()
# )

