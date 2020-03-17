import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,1000,size=(3,3)), columns=list('ABC'))
# df['B'] = '=INDIRECT("R[0]C[%s]", 0)+INDIRECT("R[0]C[%s]", 0)'%\
#           (df.columns.get_loc('A') - df.columns.get_loc('B'),
#            df.columns.get_loc('C') - df.columns.get_loc('B'))

df['B'] = '=INDIRECT("R[0]C[-1]", 0)+INDIRECT("R[0]C[1]", 0)'
with pd.ExcelWriter(r'output.xlsx', engine='openpyxl', mode='w')as writer:
    df.to_excel(writer, sheet_name='Sheet1',  index=False)