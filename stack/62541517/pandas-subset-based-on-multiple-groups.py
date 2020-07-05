import pandas as pd

df = pd.DataFrame({'year':['1979','1986','1979','1991','1964','1964'],'music' : ['Rock', 'Metal', 'Rock', 'Metal', 'Jazz', 'Jazz'], 'group' : ['Pink Floyd', 'Metallica', 'Kiss', 'Metallica', 'Coltrane', 'Coltrane'], 'songs' : ['The wall','Master of puppets','I was made for lovin you', 'Unforgiven','A love supreme','Crescent']})

def f_s(year = None, genre = None, column_name = None, row_name = None):
    a = pd.to_datetime(df[df.columns[0]])
    df[df.columns[0]] = a
    df.set_index(year, inplace = True)
    dfs = df[year]
    for j in range(len(dfs[dfs.columns[0]])):
        for k in range(len(dfs.columns)):
            if dfs.columns[k] == "music":
                if tournament == dfs[dfs.columns[k]][j]:
                    if len(dfs[dfs[dfs.columns[k]] == genre]) == 0:
                        raise ValueError
                    else:
                        dfs[dfs[d.columns[k]] == genre]
    return dfs[dfs[dfs.columns[k]] == genre].groupby(column_name).get_group(row_name)

print(f_s("1979", "Rock", "group", "Pink Floyd"))