import pandas as pd
import numpy as np

final_data = pd.DataFrame([['2019-12-04','00','ABC','2019-12-04','01','ABC','2019-12-04','02','ABC'],
                           ['2019-12-04','00','ABCD','2019-12-04','01','ABCD','2019-12-04','02','ABCD'],
                           ['2019-12-04','00','ABCDEF','2019-12-04','01','ABCDE','2019-12-04','02','ABCDEF'],
                           ['2019-12-04','03','ABCDEFG','2019-12-04','01','ABCDEFG','2019-12-04','02','ABCDEF']],
                          columns=['Date_1','Hour_1','id_1','Date_2','Hour_2','id_2','Date_3','Hour_3','id_3'])

final_export = final_data
final_export['id_2'] = final_data['id_1'] == final_data['id_2']
final_export['id_3'] = final_data['id_1'] == final_data['id_3']
print(final_export)