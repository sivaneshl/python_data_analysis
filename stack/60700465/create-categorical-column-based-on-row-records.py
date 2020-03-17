import pandas as pd
import numpy as np

ray = pd.DataFrame([[8493.000000, 'RR44', np.NaN],
                    [0.140065, 3.03E-02, 0.332000],
                    [0.143124, 3.00E-02, 0.333307],
                    [8493.000000, 'RR47', np.NaN],
                    [0.140065, 3.03E-02, 0.332000],
                    [0.141788, 2.88E-02, 0.332701]],
                   columns=['X', 'Y', 'Z'])
# print(ray)

for idx, row in ray.iterrows():
    if pd.isnull(row['Z']):
        event, id = row['X'], row['Y']
    else:
        ray.at[idx, 'event'] = event
        ray.at[idx, 'id'] = id

ray = ray[ray['Z'].isnull()==False]
print(ray)

