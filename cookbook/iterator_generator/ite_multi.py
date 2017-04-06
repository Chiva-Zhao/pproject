# 同时迭代多个序列
# 同时迭代多个序列，每次分别从一个序列中取一个元素
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)
# zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中 x 来自 a， y 来自 b。一
# 旦其中某个序列到底结尾，迭代宣告结束。因此迭代长度跟参数中最短序列长度一致
from itertools import zip_longest

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip_longest(a, b):
    print(i)
for i in zip_longest(a, b, fillvalue=0):
    print(i)
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)
print(zip(a, b))
print(list(zip(a, b)))
