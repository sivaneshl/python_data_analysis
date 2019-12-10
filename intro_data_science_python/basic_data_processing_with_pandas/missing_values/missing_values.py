import pandas as pd


df = pd.read_csv("C:/python_data_analysis/resources/course1_downloads/log.csv")
print(df)

# set time field as index and sort
df = df.set_index("time")
df = df.sort_index()
print(df)

# promote user name as a second level index (multi index) because time is not unique index
df = df.reset_index()
df = df.set_index(['time', 'user'])
df = df.sort_index()
print(df)

# fill missing values using forward fill
df = df.fillna(method='ffill')
print(df)