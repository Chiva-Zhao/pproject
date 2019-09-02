# arrayindex
from numpy import array

data = array([11, 22, 33, 44, 55])
print(data[0], data[4])
print(data[-5], data[-1])
# Two-Dimensional Indexing
data2 = array([
    [11, 22],
    [33, 44],
    [55, 66]])
print(data2[1, 1], data2[2, 1])
print(data2[1,])
print(data2[:, 1])
# Array Slicing
print(data[:])
print(data[0:1])
print(data[-2:])
# Two-Dimensional Slicing
data3 = array([
    [11, 22, 77],
    [33, 44, 88],
    [55, 66, 99]])
# separate data
x, y = data3[:, :-1], data3[:, -1]
print(x)
print(y)
split = 2
train, test = data3[:split, :], data3[split:, :]
print(train, test)

# Array Reshaping
# Reshape 1D to 2D Array
reshaped = data.reshape((data.shape[0], 1))
print(reshaped)
print(reshaped.shape)
# Reshape 2D to 3D Array
reshaped2 = data2.reshape((data2.shape[0], data2.shape[1], 1))
print(reshaped2)
print(reshaped2.shape)
# dot multiplication
a = array([1, 2, 3])
b = array([1, 2, 3])
print(a.dot(b))
c = 5 * a
print(c)
# L1 norm
from numpy.linalg import norm

L1 = norm(a, 1)
# L2 norm
L2 = norm(a, 2)
print(L1, L2)
# max norm
from math import inf

LMax = norm(a, inf)
print(LMax)
