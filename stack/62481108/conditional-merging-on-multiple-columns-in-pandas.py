import pandas as pd

df = pd.DataFrame({'FULL ADDRESS': ['123 MAIN STREET COLLEGEVILLE PA 19426',
                                    '527 W DEKALB PIKE KING OF PRUSSIA PA 19406',
                                    '1800 NORTH AVE KING OF PRUSSIA PA 19406',
                                    '673 ADDRESS1 ADDRESS2 19403'],
                   'ADDRESS1': ['123', '587', '1800', '673'],
                   'ADDRESS2': ['MAIN STREET', 'W DEKALB PIKE', 'NORTH AVE', 'ADDRESS1'],
                   'ADDRESS3': ['COLLEGEVILLE', 'KING OF PRUSSIA', 'KING OF PRUSSIA', 'ADDRESS2'],
                   'ADDRESS4': ['PA', 'PA', 'PA', ''],
                   'POSTCODE': ['19426', '19406', '19406', '19403']})
df1 = pd.DataFrame({'FULL ADDRESS': ['123 MAIN STREET COLLEGEVILLE PA 19426',
                                     '527 W DEKALB PIKE KING OF PRUSSIA PA 19406',
                                     '1800 NORTH AVE KING OF PRUSSIA PA 19406',
                                     '673 ADDRESS1 ADDRESS2 19403']})

print(pd.merge(df, df1, on='FULL ADDRESS'))