import pandas as pd

df = pd.DataFrame([['01','001',0.000332,0.000328,-0.000004],
                   ['01','003',0.000617,0.000748,0.000131],
                   ['01','005',0.000534,0.000440,-0.000094],
                   ['01','007',0.000241,0.000158,-0.000084]],
                  columns=['state','county','density_10_722513','density_15_722513','density_diff'])

print(df)