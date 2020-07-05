import pandas as pd

name=['Charge','charge','Prepaid']
lemma=['Hallo','hallo','Hi']

df = pd.DataFrame([['Bob', 'Charge', 'E333', 'B442'],
              ['Karen', 'V434', 'Prepaid', 'B442'],
              ['Jill', 'V434', 'E333', 'charge'],
              ['Hank', 'Charge', 'E333', 'B442']],
             columns=['Name', 'ID_First', 'ID_Second', 'ID_Third'])

df=df.replace(name, value=lemma)
print(df)
