import matplotlib.pyplot as plt
import numpy as np

# scatterplots takes an x axis value as first arg and y axis value as 2nd arg
x = np.array([1,2,3,4,5,6,7,8])
y = x

plt.figure()
plt.scatter(x, y)
plt.show()

# add colors
colors = ['green']*(len(x)-1)   # one short than the array size
colors.append('red')    # last one to red
plt.scatter(x, y, s=100, c=colors)  # size=100 and colors=colors array
plt.show()
