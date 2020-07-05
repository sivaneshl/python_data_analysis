import pandas as pd

dt = pd.DataFrame({'name': ['John', 'Jane', 'John', 'Smith', 'Jane', 'Smith', 'Tom', 'Gary', 'Tom', 'John'],
                   'date': ['01-01-2020', '02-01-2020', '03-01-2020', '03-01-2020', '03-01-2020','03-01-2020','03-01-2020','03-01-2020','03-01-2020','03-01-2020']})

dt['id'] = dt.groupby(dt.name.tolist(), sort=False).ngroup() + 1

print(dt)