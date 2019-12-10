import numpy as np

# operations using numpy arrays

# element wise addition, subtraction etc
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)
print(x - y)
print(x**2)


# linear algebra dot product
print(x.dot(y))

# transpose array
z = np.array([y, y**2])
print(z)
print(z.shape)
print(z.T)
print(z.T.shape)

# dtype function - get what type the array has
print(z.dtype)
# astype function - cast an array to a type
z = z.astype('f')
print(z.dtype)

# math fucntions
a = np.array([-4, -2, 1, 3, 5])
print(a.sum())
print(a.max())
print(a.min())
print(a.mean())
print(a.std())

# to find the index of the max or min value
print(a.argmax())
print(a.argmin())

