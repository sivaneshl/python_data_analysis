import pandas as pd

SpeciesList = pd.DataFrame({'Code': ['Cencili', 'Eucpopu '],
                            'Scientific': ['Cenchrus ciliaris*','Eucalyptus populnea']})
SpeciesDict = dict(zip(SpeciesList.Code, SpeciesList.Scientific))

print(SpeciesList.Scientific.replace(r'\*', 'test', regex=True))