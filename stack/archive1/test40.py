import pandas as pd
import difflib

df1 = pd.DataFrame ({'Restaurant_Name': ['Apple', 'Banana', 'Orange', 'apple','apple1'],
                     'Postal Code': [12345, 12345, 54321, 54321,1111]})
df2 = pd.DataFrame ({'Restaurant_Name': ['apple', 'apple', 'Banana', 'Pineapple'],
                     'Postal Code': [12345, 54321, 12345, 12345],
                     'Phone':[100,200,300, 400]})

df1['key'] = df1['Restaurant_Name']+df1['Postal Code'].astype(str)
df2['key'] = df2['Restaurant_Name']+df2['Postal Code'].astype(str)
df2['key'] = df2['key'].apply(lambda x: difflib.get_close_matches(x, df1['key'])[0])
df2['score'] = difflib.SequenceMatcher(None, df1['key'], df2['key']).ratio()

print(
    df1.merge(df2, on='key', how='outer')[['Restaurant_Name_x','Restaurant_Name_y','Postal Code_x','Phone', 'score']]
)