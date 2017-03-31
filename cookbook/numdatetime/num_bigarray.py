# 大型数组运算
# 涉及到数组的重量级运算操作，可以使用 NumPy 库。 NumPy 的一个主要特征是它会给 Python 提供一个数组对象，
# 相比标准的 Python 列表而已更适合用来做数学运算
# python list
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x * 2)
# print(x+10)
print(x + y)
# numpy array
import numpy as np

ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2, ax + 10, ax + ay, ax * ay)
print(np.sqrt(ax), np.cos(ax))
# 使用这些通用函数要比循环数组并使用 math 模块中的函数执行计算要快的多。因
# 此，只要有可能的话尽量选择 NumPy 的数组方案。
# 底层实现中， NumPy 数组使用了 C 或者 Fortran 语言的机制分配内存。也就是说，
# 它们是一个非常大的连续的并由同类型数据组成的内存区域。所以，你可以构造一个
# 比普通 Python 列表大的多的数组。比如，如果你想构造一个 10,000*10,000 的浮点数
# 二维网格
grid = np.zeros(shape=(10000, 10000), dtype=float)
grid += 10
# print(np.sin(grid))
# 关于 NumPy 有一点需要特别的主意，那就是它扩展 Python 列表的索引功能
# - 特别是对于多维数组
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
# Select row 1
print(a[1])
# select column 1
print(a[:, 1])
# Select a subregion and change it
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a)
# Broadcast a row vector across an operation on all rows
print(a + [100, 101, 102, 103])
# Conditional assignment on an array
print(np.where(a < 10, a, 10))
