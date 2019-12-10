import pandas as pd

tableA = pd.DataFrame([[1,'Tom','01/12/80',29382],
                       [2,'Kate','21/2/90',39383],
                       [3,'Ini','23/8/92',28287]],
                      columns=['ID','Name','Birthday','Salary'])

tableB = pd.DataFrame([[1,'Tom','01/12/80','Chur'],
                       [2,'Kate','21/2/90','Blu'],
                       [3,'Ini','23/8/92','La']],
                      columns=['ID','Name','Birthday','Home'])

# merge1=(pd.merge(tableA, tableB, how = 'inner', on =['ID']))
# print(merge1)
# print(merge1[['ID','Name','Birthday','Salary','Home']])

join_table = tableA.merge(tableB[['ID','Home']], how = 'left', on =['ID'])
print(join_table)

