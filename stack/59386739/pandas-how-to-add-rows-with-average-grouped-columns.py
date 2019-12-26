import numpy as np
import pandas as pd

fruit = ['apple', 'apple', 'banana', 'banana', 'kiwi', 'kiwi', 'grape', 'grape']
ftype = ['one', 'two', 'one', 'two', 'three', 'one', 'one', 'two']
resource = ['us', 'us', 'us', 'us', 'us', 'us', 'us', 'us']
price = [100, 150, 200, 300, 120, 300, 400, 500]
df = pd.DataFrame({'fruit': fruit, 'ftype': ftype, 'resource': resource, 'price': price})


print(df)