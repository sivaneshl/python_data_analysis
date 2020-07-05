import pandas as pd

df = pd.DataFrame({'user': ['one', 'two', 'three', 'four'],
                   'tags': [set(), set(), set(), set()]})
df.set_index('user', inplace=True)

def add_tag(user, tag):
    df.loc[user]['tags'].add(tag)

add_tag('two', 'happy')
add_tag('two', 'friendly')
add_tag('two', 'friendly')

print(df)