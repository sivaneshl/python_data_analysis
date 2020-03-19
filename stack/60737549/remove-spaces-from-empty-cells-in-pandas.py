import pandas as pd

df = pd.DataFrame({'col1': [' ', ' ', ' ']})
print(df)
df.col1 = df['col1'].str.replace(' ','')
print(df)