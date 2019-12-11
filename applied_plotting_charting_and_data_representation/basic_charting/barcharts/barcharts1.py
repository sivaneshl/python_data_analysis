import numpy as np
import matplotlib.pyplot as plt

linear_data = np.array(range(1,9))
quadratic_data = linear_data**2

plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width=0.3, color='blue')

new_xvals = []
for item in xvals:
    new_xvals.append(item+0.3)
plt.bar(new_xvals, quadratic_data, width=0.3, color='red')

# plt.show()

from random import randint
linear_err = [randint(0,15) for x in range(len(linear_data))]
plt.bar(xvals, linear_data, width=0.3, yerr=linear_err)

plt.show()

