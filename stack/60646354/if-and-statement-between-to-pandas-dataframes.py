from difflib import SequenceMatcher
import pandas as pd
import numpy as np

df1 = pd.DataFrame([['Apple', 1, 5, 'Fruit'],
                    ['Banana', 2, 8, 'Fruit'],
                    ['Cat', 3, 4, 'Animal']],
                   columns=['Name','Class','Amt $','Category'])

df2 = pd.DataFrame([[1, 'Apple is Red', 1, 5, 'Fruit'],
                    [2, 'Banana', 2, 8, 'fruits'],
                    [3, 'Cat is cute', 3, 4, 'animals'],
                    [4, 'Green Apple', 1, 5, 'fruis'],
                    [5, 'Banana is Yellow', 2, 8, 'fruet'],
                    [6, 'Cat', 3, 4, 'anemal'],
                    [7, 'Apple', 1, 5, 'anemal'],
                    [8, 'Ripe Banana', 2, 8, 'frut'],
                    [9, 'Royal Gala Apple', 1, 5, 'Fruit'],
                    [10, 'Cats', 3, 4, 'animol'],
                    [11, 'Green Banana', 2, 8, 'Fruit'],
                    [12, 'Green Apple', 1, 5, 'fruits'],
                    [13, 'White Cat', 3, 4, 'Animal'],
                    [14, 'Banana is sweet', 2, 8, 'appel'],
                    [15, 'Apple is Red', 1, 5, 'fruits'],
                    [16, 'Ginger Cat', 3, 4, 'fruits'],
                    [17, 'Cat house', 3, 4, 'animals'],
                    [18, 'Royal Gala Apple', 1,5, 'fret'],
                    [19, 'Banana is Yellow', 2, 8, 'fruit market'],
                    [20, 'Cat is cute', 3, 4, 'anemal']],
                   columns=['Index', 'Name', 'Class', 'Amt $', 'Category'])

df2['match'] = ''
for idx2, row2 in df2.iterrows():
    match = ''
    for idx1, row1 in df1.iterrows():
        if (SequenceMatcher(None, row1['Name'], row2['Name']).ratio())>=0.5 and \
                (SequenceMatcher(None, row1['Category'], row2['Category']).ratio())>=0.5 and \
                (row1['Class'] == row2['Class'] or row1['Amt $'] == row2['Amt $']):
            match = row1['Name']
            break
    df2.at[idx2, 'match'] = match


print(df2[df2['match']==''].append(df2[df2['match']!=''].drop_duplicates(keep='first')))