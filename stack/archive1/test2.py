import pandas as pd


# df = pd.DataFrame([['1000', 2011, 'Type1', '2000', 2012, 'Type2', '3000', 2013, 'Type3'],
#                    ['4000', 2014, 'Type4', '5000', 2015, 'Type5', '6000', 2016, 'Type6'],
#                    ['8000', 2018, 'Type7', '8000', 2018, 'Type8', '9000', 2019, 'Type9']],
#                   columns=['salary', 'year', 'emp_type', 'salary2', 'year2', 'emp_type2', 'salary3', 'year3', 'emp_type3'])
# df = pd.DataFrame(df.values.reshape(-1,3),columns=['salary', 'year', 'emp_type'])
# print(df)


df = pd.DataFrame(['1000', 2011, 'Type1', '2000', 2012, 'Type2', '3000', 2013, 'Type3',
                   '4000', 2014, 'Type4', '5000', 2015, 'Type5', '6000', 2016, 'Type6',
                   '8000', 2018, 'Type7', '8000', 2018, 'Type8', '9000', 2019, 'Type9'])
df = pd.DataFrame(df.values.reshape(-1,3),columns=['salary', 'year', 'emp_type'])
print(df)