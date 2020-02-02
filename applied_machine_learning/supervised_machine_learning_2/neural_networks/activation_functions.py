import numpy as np
import matplotlib.pyplot as plt

xrange = np.linspace(-2, 2, 200)

fig = plt.figure(figsize=(7, 6))

plt.plot(xrange, np.maximum(xrange, 0), label='relu')
plt.plot(xrange, np.tanh(xrange), label='tanh')
plt.plot(xrange, 1 / (1 + np.exp(xrange)), label='logistic')

plt.legend()
plt.title('Neural network activation functions')
plt.xlabel('Input value (x)')
plt.ylabel('Activation function output')

plt.show()