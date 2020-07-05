import pandas as pd
import csv

rows = []
with open('test.csv', 'rt') as f:
    for row in csv.DictReader(f, fieldnames=['A', 'B', 'C', 'D', 'E']):
        if row['A'].startswith('Column') and row['B'] == 'Car Make' and row['D'] == 'Car Model':
            column, make, model = row['A'], row['C'], row['E']
            customer = fname = lname = phone = ''
        elif row['A']!='Customer':
            customer, fname, lname, phone = row['A'], row['B'], row['C'], row['D']

        if fname!='':
            rows.append([column, customer, fname, lname, phone, make, model])

df = pd.DataFrame(rows, columns=['Column', 'Customer', 'fname', 'lname', 'phone', 'Car Make', 'Car Model'])
print(df)