import pandas as pd

df = pd.DataFrame({'RFMin': [1000, 2000, 2000, 4000, 1000], 'RFMax': [3333, 5125.5, 8800, 6000, 3000]})
MG = pd.DataFrame({'RFMin': [660, 2700, 8600], 'RFMax': [750, 4000, 16000]})

for idx1, row1 in df.iterrows():
    for idx2, row2 in MG.iterrows():
        if row1.RFMin < row2.RFMin and row2.RFMin < row1.RFMax < row2.RFMax:
            print('Number is Overlapping at beginning', ((row1.RFMax - row2.RFMin) / (row1.RFMax - row1.RFMin)))
        if row2.RFMin > row1.RFMin > row2.RFMax and row2.RFMin > row1.RFMax < row2.RFMax:
            print('Number is in between given range ')
        if row2.RFMin < row1.RFMin < row2.RFMax and row1.RFMax > row2.RFMax:
            print('Number is overlapping at the end', ((row2.RFMax - row1.RFmin) / (row1.RFMax - row1.RFMin)))



