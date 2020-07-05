import pandas as pd
import statistics as st

file = pd.read_excel("alcohol.xls").sort_values("X")
index_row = [i+1 for i in range(len(file))]
index_new = pd.Index(index_row)
column_df = pd.DataFrame(file.loc[:,"X"])
new = column_df.set_index(index_new)


def median_1(table):
    print(table.median())


def median_2(table):
    print(st.median(table))


median_1(new['X'])
median_2(new['X'])

print(st.median(new))