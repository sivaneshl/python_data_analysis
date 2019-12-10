import pandas as pd
import numpy as np


df = pd.DataFrame(data=np.random.randint(0, 2, size=(1000, 11)),
                  columns=["attr"+str(i+1) for i in range(10)] + ["y"])

print(df)
