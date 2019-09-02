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
