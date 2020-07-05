import pandas as pd

col = ['Rank', 'Country']

df = pd.read_excel('C:/python_data_analysis/intro_data_science_python/resources/course1_downloads/scimagojr-3.xlsx',
                    sheet_name=None, usecols=col)

print(df)