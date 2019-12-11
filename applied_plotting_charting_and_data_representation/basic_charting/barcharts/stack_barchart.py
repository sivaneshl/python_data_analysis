import numpy as np
import matplotlib.pyplot as plt

linear_data = np.array(range(1,9))
quadratic_data = linear_data**2

plt.figure()
xvals = range(len(linear_data))

plt.bar(xvals, linear_data, width=0.3)
plt.bar(xvals, quadratic_data, bottom=linear_data, width=0.3, color='red')

plt.show()