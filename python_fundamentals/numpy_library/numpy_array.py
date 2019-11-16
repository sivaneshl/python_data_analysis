import numpy as np

# creating arrays
# convert list to an array using numpy
mylist = [1, 2, 3]
x = np.array(mylist)
print(x)

# using the list directly
x = np.array([4,5,6])
print(x)

# multi-dimensional array
md = np.array([[1, 2, 4], [4, 5, 6]])
print(md)
# get the dimensions using shape attribute
print(md.shape)

# arrange function - we pass a start, stop and a step
# it will return a list evenly spaced ineterval
x = np.arange(0, 30, 2)
print(x)
# arange also can be
x2 = np.arange(6)
print(x2)

# reshape function - convert this array of numbers to a x-by-y array
print(x.reshape(3, 5))
print(x)

# linspace function is similar to arrange, but instead of step we tell it how many numbers we want to return
l = np.linspace(0, 4, 9)
print(l)

# resize to change the dimensions
l.resize(3, 3)
print(l)

# create array of one's
o = np.ones((3, 3))
print(0)

# create array of zero's
z = np.zeros((3, 3))
print(z)

# create array of 1's and 0's
e = np.eye(3)
print(e)

# create diagonal array
d = np.diag([4, 5, 6])
print(d)

# create an array with repeated values
# using array
ra = np.array([1, 2, 3] * 3)
print(ra)
#using repeat
rr = np.repeat([1, 2, 3], 3)
print(rr)

# create a 2X3 array of 1s and vertical stack it on 2s array
p = np.ones((2, 3), int)
print(p)
v = np.vstack([p, 2*p])
print(v)
# stacking horizontally
h = np.hstack([p, 2*p])
print(h)


