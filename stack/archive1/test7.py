import pandas as pd
import numpy as np

mylist = [
    (1, "I like fruits"),
    (2, "I like meat"),
    (3, "This is only test"),
    (4, "This is being tested"),
    (5, "lorem ipsum"),
    (6, "I like flowers"),
]

df = pd.DataFrame(mylist)
df.columns = ["sr_no", "text_original"]

mylist1 = [
    (1, "I like fruits", "I like meat", 91),
    (1, "I like fruits", "This is only test", 21),
    (2, "I like meat", "I like fruits", 91),
    (3, "This is only test", "This is being tested", 95),
    (3, "This is only test", "I like fruits", 15),
    (4, "This is being tested", "This is only test", 95),
    (5, "lorem ipsum", "This is being tested", 11),
    (5, "lorem ipsum", "I like fruits", 12),
    (6, "I like flowers", "I like fruits", 99),
]

df1 = pd.DataFrame(mylist1)
df1.columns = ["sr_no", "text_original", "text_compare", "co_similar"]
print(df1[df1['co_similar']>90])

# datadf['new_col'] = datadf.apply(lambda x: (np.where((x['country'] == configdf['country']) & (x['business'] == configdf['business']))[0][0]),axis=1)
df['new_col'] = df.apply(lambda x: (np.where((x['text_original'] == df1['text_original']) or (x['text_original'] == df1['text_compare']))[0][0]),axis=1)
print(df)

