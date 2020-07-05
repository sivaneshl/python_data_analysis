import pandas as pd

df = pd.DataFrame({'Col1':list('abcdeafgbfhi')})

search_str = 'b'

idx_list = list(df[(df['Col1']==search_str)].index.values)

print(df[idx_list[0]:idx_list[1]])