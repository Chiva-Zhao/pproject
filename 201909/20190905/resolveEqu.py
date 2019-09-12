# 7x + 5y -3z = 16
# 3x - 5y + 2z = -8
# 5x + 3y - 7z = 0
import numpy as np

A = np.array([[7, 5, -3], [3, -5, 2], [5, 3, -7]])
print(A)
b = np.array([16, -8, 0])
# x = np.linalg.lstsq(A, b, rcond=None)[0]
x = np.linalg.solve(A, b)
print(x)
print(np.allclose(A.dot(x), b))
