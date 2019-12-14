import matplotlib.pyplot as plt
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2

plt.figure()
plt.subplot(1, 2, 1)    # 1 row with 2 columns and the 1st sub plot will be the active plot
plt.plot(linear_data, '-o')

plt.subplot(1, 2, 2)    # 1 row with 2 columns and the 2nd sub plot will be the active plot
plt.plot(exponential_data, '-o')

plt.show()
