import pandas as pd


# read from olympics.csv using the pandas function read_csv to a data frame
df = pd.read_csv("C:/python_data_analysis/resources/course1_downloads/olympics.csv")
print(df.head())

# use options for read_csv function
# set the column 0 (country) as index
# skip the 1st row
df = pd.read_csv("C:/python_data_analysis/resources/course1_downloads/olympics.csv",
                 index_col=0,
                 skiprows=1)
print(df.head())


# pandas store the column names in the .columns attribute
print(df.columns)
# we can rename the columns names by iterating through this list and rename
for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col:'#'+col[2:]}, inplace=True)
print(df.head())