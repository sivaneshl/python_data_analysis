import pandas as pd

df = pd.DataFrame({'A': [['KB4525236', 'KB4485447', 'KB4520724', 'KB3192137', 'KB4509091']], 'B': [['a', 'b']]})

findKBs = ['KB4525236','KB4525202']
df['C'] = [[x for x in findKBs if x not in df['A'][0]]]
print(df)