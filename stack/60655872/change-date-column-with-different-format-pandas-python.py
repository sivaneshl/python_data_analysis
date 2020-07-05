import pandas as pd

df = pd.DataFrame({'date': ['01.01.2001', '1.01.2001', '01.1.2001', '1.1.2001', '1.01.01', '010101', '1.1.01',
                            '01012001']})
# , '01.2001', '1.2001',
#                             '01012001', '01.01', , , '1.1.01']})
print(pd.to_datetime(df['date'], dayfirst=True, errors='coerce'))
print(pd.to_datetime('01.2001', format = '%m.%y'))