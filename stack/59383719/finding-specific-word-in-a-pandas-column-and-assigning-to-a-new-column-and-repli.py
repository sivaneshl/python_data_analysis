import pandas as pd
import numpy as np
import re

data={ 'ID':['351362278576','351539320880','351582465214','351609744560','351708198604'],
       'BU':['SBS','MAS','NAS','ET','SBS'],
       'Comment':['940/941/w2-W3NYSIT/SUI33/3305/2019/1q',
                  'OK SUI 2Q19',
                  '941 - 3Q2019NJ SIT - 3Q2019NJ SUI/SDI - 3Q2019',
                  'IL,SUI,2016Q4,2017Q1,2017Q2',
                  '1Q2019 PA 39/5659 39/2476']}
wizard = pd.DataFrame(data)


test_set = {'941', '942'}
test_set2={'MN','OK','33/3305'}
wizard['ZTYPE'] = wizard['Comment'].apply(lambda x: re.split(', |- ', x))
wizard['ZJURIS'] = wizard['Comment'].apply(lambda x: any(i in test_set2 for i in x.split()))
# wizard['commentsplit'] = re.split(',', wizard['Comment'].str)

print(wizard)