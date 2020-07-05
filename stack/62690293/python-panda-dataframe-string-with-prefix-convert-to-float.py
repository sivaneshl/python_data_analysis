import pandas as pd

df = pd.DataFrame({'col': ['0.02u\n', '0.1\n', '2.02n\n']})
u = 10^(-6)
n = 10^(-9)

# Remove the \n characters
df['col'] = df['col'].replace(to_replace="\n", value="", regex=True)
# Put '*' for multiplication --> '3x' will be converted to '3*x'
df['col'] = df['col'].replace(to_replace=r"((?:\d+)|(?:[a-zA-Z]\w*\(\w+\)))((?:[a-zA-Z]\w*)|\()",
                              value=r"\1*\2", regex=True)
df['val'] = pd.eval(df['col'])
print(df)