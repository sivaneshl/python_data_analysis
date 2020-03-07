import pandas as pd
import datetime as dt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

def parse(datestr):
    y,m,d = datestr.split("-")
    return dt.date(int(y),int(m),int(d))

df = pd.read_excel('text.xlsx', header=None, converters={2:str})

print(df)