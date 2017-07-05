#
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def step_function(x):
    return np.array(x > 0, dtype=np.int)


#call step funcion
x = np.arange(-5.0, 5.0, 0.1)
y1 = step_function(x)


#x = np.arange(-15.0, 15.0, 0.01)
#x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x,y, label="sigmoid")
plt.plot(x,y1, linestyle="--", label="step_fun")
plt.ylim(-0.1, 1.1)
plt.title('sigmoid function ( 1/(1 + exp(-x))')
plt.xlabel("x")
#plt.ylabel("sigmoid(x)")
plt.legend()
plt.show()