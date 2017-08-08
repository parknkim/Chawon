import numpy as np
import matplotlib.pyplot as plt

step = 0.1
low = -2*np.pi
high = 2*np.pi

#x = np.arange(0, 6, 0.1)
x = np.arange(low, high, step)
y = np.sin(x)

plt.plot(x, y)
plt.show()