import numpy as np

# create a 4X3 array of random int from 1 to 10
test = np.random.randint(0, 10, (4, 3))
print(test)

# iterate rows
for row in test:
    print(row)

for i in range(len(test)):
    print(test[i])

# enumarate will give the index and row
for i, row in enumerate(test):
    print('row', i, 'is', row)

# loop through 2 arrays using zip
test2 = test**2
print(test2)
for i, j in zip(test, test2):
    print(i, '+', j, '=', i + j)