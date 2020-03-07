import pandas as pd

df = pd.DataFrame(columns=["Date", "Title", "Artist"])

df.insert(loc=0, column="Date", value=dateTime.group(0), allow_duplicates=True)
df.insert(loc=0, column="Title", value=title, allow_duplicates=True)
df.insert(loc=0, column="Artist", value=artist, allow_duplicates=True)

print(df)