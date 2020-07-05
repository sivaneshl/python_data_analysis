import pandas as pd

BAU_DYNAMIC_DF = pd.DataFrame()
ML_DYNAMIC_DF = pd.DataFrame()
RANDOM_DF = pd.DataFrame()

group_keys = ['BAU_DYNAMIC', 'ML_DYNAMIC', 'RANDOM']

for k,value in enumerate(group_keys):
    if value == 'BAU_DYNAMIC':
        BAU_DYNAMIC_DF = pd.concat([BAU_DYNAMIC_DF,group_df[k]])
    elif value == 'ML_DYNAMIC':
        ML_DYNAMIC_DF = pd.concat([ML_DYNAMIC_DF,group_df[k]])
    else:
        RANDOM_DF = pd.concat([RANDOM_DF,group_df[k]])

print(BAU_DYNAMIC_DF)