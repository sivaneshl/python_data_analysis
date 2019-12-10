import numpy as np

# create an array with the squares of 0 through 12
a = np.arange(13)**2
print(a)

# to get a value at a particular index
print(a[0], a[4])
# to get a range use colon notation
print(a[1:4])

# slice of the last 4 elements of the array
print(a[-4:])

# slice 5th from the end till the beginning of the array counting backwards by 2
print(a[-5::-2])

# extending to a 2-dim array
# create a 2d array
r = np.arange(36)
r.resize(6, 6)
print(r)
# get the 2nd row 2nd col element
print(r[2, 2])
# get 3rd row colums 3 to 6
print(r[3, 3:6])
# getfirst 2 rows except except last col
print(r[:2, :-1])
# get every 2nd element from the last row
print(r[-1, ::2])

# bracket operator
# get the elements from our original array that are greater than 30
print(r[r > 30])
# take the elements > 30 and assign them a new value
r[r > 30] = 30
print(r)

# copying data
# create a new array r2 by slicing from r
r2 = r[:3, :3]
print(r2)
# assign all the elements of r2 to 0
r2[:] = 0
print(r2)
# now the sliced elements from the original array r are also changed
print(r)

# create a copy using copy()
# changing the values of the copied array, the original array remains unchanged
r_copy = r.copy()
r_copy[:] = 10
print(r_copy)
print(r)