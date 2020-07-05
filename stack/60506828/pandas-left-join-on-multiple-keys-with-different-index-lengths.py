import pandas as pd

df1 = pd.DataFrame({'Month': [1,1,1,1,1,2,2,2,2,2],
                    'Plant': ['A','A','A','B','B','A','A','A','B','B'],
                    'Product': ['AFS','TF1','AA1','AA1','POD','AFS','TF1','AA1','AA1','POD'],
                    'Production': [11212, 9005, 21656, 11512, 6550, 12550, 12121, 15091, 16212, 7890]})
df2 = pd.DataFrame({'Month': [1,1,1,1,1,1,2,2,2],
                    'Product': ['AFS','AA1','TF1','POD','ZBR','TPO','AFS','AA1','TF1']})

print(df1.groupby([['Month','Plant','Procduct']])['Production'])