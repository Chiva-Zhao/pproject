# 矩阵与线性代数运算
import numpy as np
import numpy.linalg

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
# Create a vector and multiply
v = np.matrix([[2], [3], [4]])


def base():
    # print(m, m.T, m.I, sep='\n')
    print(v, m * v, sep='\n')


def lineagle():
    print(numpy.linalg.det(m))
    # Eigenvalues
    print(numpy.linalg.eigvals(m))
    # Solve for x in mx = v
    x = numpy.linalg.solve(m, v)
    print(x, m * x, sep='\n')


lineagle()
