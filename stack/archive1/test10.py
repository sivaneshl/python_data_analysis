import pandas as pd
import numpy as np

df = pd.DataFrame([['TP','Model1','0.73'],
                   ['TN','Model1','0.27'],
                   ['FN','Model2','0.24'],
                   ['TP','Model2','0.58'],
                   ['TN','Model2','0.18']],
                  columns=['confusion_matrix_group','model','proportion'])

# print(df[['confusion_matrix_group', 'model']].values,
#       type(df[['confusion_matrix_group', 'model']].values))

for group in ['TP', 'TN', 'FP', 'FN']:
    for model in np.unique(df.model):
        if [group, model] not in df[['confusion_matrix_group', 'model']].values.tolist():
            df=df.append(pd.Series({'confusion_matrix_group': group, 'model': model, 'proportion': 0}),ignore_index=True)

print(df)
