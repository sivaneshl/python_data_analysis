import pandas as pd
import numpy as np

df = pd.DataFrame(['Date','Clinic','Location','Clinic Manager','Lease Cost','Square Footage','Lease Expiration',
                   np.NaN,'Care Provided','# of Providers (Full Time)','# FTEs Providing Care',
                   '# Providers (Part-Time)','Patients seen per week','Number of patients in rooms per provider',
                   'Number of patients in waiting room','# Exam Rooms','Procedure rooms','Other rooms','Specify other',
                   np.NaN,'Other data:','TI Needs:',np.NaN,'Conclusion  & Recommendation','9/13/2017',
                   'Thornton Medical Center','5000 E. 66th Ave Thornton CA 12345','Jane Doe',
                   '$23,074.80 Rent, $5,392.88 CAM',9,840,'7/31/2023',np.NaN,'Family Medicine',12,14,1,750,4,2,31,
                   1,'X-Ray, Phlebotomist/blood draw',np.NaN,
                   'Facilities assistance needed.  50% of business...',
                   'Paint and Carpet (flooring is in good conditio...',np.NaN,
                   'Lay out and occupancy flow are good for this p...'])

# df2 = pd.DataFrame(columns=df.columns[:23])
# df2 = np.reshape(df.loc[25:].values, (1, 23))
# print()
df2 = pd.DataFrame(df[24:].values.reshape(-1, 24),
                   columns=df[:24][0])
print(df2)