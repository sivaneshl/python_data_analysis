import pandas as pd
import numpy as np

list_arrays=np.array([[1, 2, 4], [4, 5, 6], [7, 8], [9, 10, 11, 12], [13, 14, 15, 16, 17, 18]])
list_arrays=np.array([i + [np.NaN]*((len(max(list_arrays)))-len(i)) for i in list_arrays])
df=pd.DataFrame(list_arrays)

print(df)