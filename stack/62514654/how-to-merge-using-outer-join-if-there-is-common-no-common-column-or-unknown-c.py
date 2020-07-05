import pandas as pd
import numpy as np

df_a = pd.DataFrame({
    "bookid": ["12345", "789"],
    "bookname": ["who am i", "i am jack"]
})
df_b = pd.DataFrame({
    "bookid": ["12345", np.NaN],
    "bookname": ["who am i", "i am jack"],
    "Author" : ["asp", "ppp"]
})

_, df_a = df_b.align(df_a, fill_value=np.NaN)
_, df_b = df_a.align(df_b, fill_value=np.NaN)
# print(df_a)
# print(df_b)


# for col in df_b.columns:
#     df_temp = pd.merge(df_a[[col]], df_b[[col]], left_index=True, right_index=True)
#     df_temp['diff'] = np.where((df_temp[col+'_x'] == df_temp[col+'_y']), 'No', 'Yes')
#     print(df_temp)

# df1 = pd.merge(df_a[['bookid']], df_b[['bookid']], left_index=True, right_index=True)
# df1['diff'] = np.where((df1['bookid_x']==df1['bookid_y']), 'No', 'Yes')
#
# df2 = pd.merge(df_a[['bookname']], df_b[['bookname']], left_index=True, right_index=True)
# df2['diff'] = np.where((df2['bookname_x']==df2['bookname_y']), 'No', 'Yes')
#
# df3 = pd.merge(df_a[['Author']], df_b[['Author']], left_index=True, right_index=True)
# df3['diff'] = np.where((df3['Author_x']==df3['Author_y']), 'No', 'Yes')
#
# print(df1)
# print(df2)
# print(df3)

# df_temp = pd.merge(df_a, df_b, left_index=True, right_index=True)
# with open(r"booktest.html", 'w') as _file:
#     for col in df_a.columns:
#         df_temp[col+'_diff'] = np.where((df_temp[col+'_x'] == df_temp[col+'_y']), 'No', 'Yes')
#         _file.write(df_temp[[col + '_x', col + '_y', col + '_diff']].to_html(index=False) + "<br>")
# print(df_temp)

text_align = '<style>.dataframe td { text-align: right; width: 40;}</style>'
with open(r"booktest.html", 'w') as _file:
    for col in df_a.columns:
        df_temp = pd.DataFrame()
        df_temp[col + '_current'], df_temp[col + '_future'], df_temp[col + '_diff'] = df_a[col], df_b[col], np.where((df_a[col] == df_b[col]), 'No', 'Yes')
        # df_temp.dropna(how='all', axis=1, inplace=True)
        [df_temp.rename(columns={c:''}, inplace=True) for c in df_temp.columns if df_temp[c].isnull().all()]
        df_temp.fillna('', inplace=True)
        with pd.option_context('display.max_colwidth', -1):
            _file.write(text_align+df_temp.to_html(index=False) + "<br>")
        print(df_temp)
