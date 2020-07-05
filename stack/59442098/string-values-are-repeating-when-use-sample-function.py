import pandas as pd
import numpy as np

from pandas import Series,DataFrame

CHCbot_Emp = DataFrame({'Employee_Name':['Deepak','Varadharajan','Akash','Jeffrin','Ashwini','Sathish','Vikram','Narasiman','satyavathi'],
                       'Employee_Code':['IS4001','IS4002','IS4003','IS4004','IS4005','IS4006','IS4007','IS4008','IS4009']})
# print(CHCbot_Emp)

l = list(range(len(CHCbot_Emp)))
np.random.shuffle(l)
print(l)

for rows in CHCbot_Emp.itertuples(index=False):
    print(rows.Employee_Name+" "+rows.Employee_Code)
    print('Hey '+rows.Employee_Name+'!!! Pick your Child')
    random_Variable = CHCbot_Emp.iloc[l.pop()]
    print(random_Variable.Employee_Code+" "+random_Variable.Employee_Name)