import pandas as pd

df = pd.read_excel(open('text.xlsx','rb'))
# print(df)


df = df.dropna(how='all').dropna(how='all', axis=1)
df['Groups'] = df['Groups'].fillna(method='ffill')
df.dropna(inplace=True)

print(df.groupby('Groups')['Letters'].apply(list).to_dict())