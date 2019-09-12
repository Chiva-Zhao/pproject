import numpy as np
from numpy.linalg import lstsq
from matplotlib import pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])
A = np.vstack((x, np.ones(len(x)))).T
B = np.vstack([x, np.ones(len(x))]).T
m, c = lstsq(B, y, rcond=None)[0]
print(m, c)
plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m * x + c, 'r', label='Fitted line')
plt.legend()
plt.show()
