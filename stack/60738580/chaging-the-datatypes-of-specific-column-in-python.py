import pandas as pd


df = pd.read_excel('text.xlsx')
print([(col, type(col)) for col in df.columns])
# cols = df.columns
# cols[2:] = cols[2:].map(lambda x: x.strftime('%Y-%m-%d'))
# print(df.columns.map(type))
df.columns = df.columns.astype(str)
# print(df.columns.map(type))
print([(col, type(col)) for col in df.columns])