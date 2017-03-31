# 你想创建或测试正无穷、负无穷或 NaN(非数字) 的浮点数。
# Python 并没有特殊的语法来表示这些特殊的浮点值，但是可以使用 float() 来创建它们
a = float('inf')
b = float('-inf')
c = float('nan')
d = float('nan')
import math


def simple():
    print(a, b, c)
    print(math.isinf(a), math.isnan(c))
    print(a + 45, a * 10, 10 / a)
    print(a / a, a + b, c + 23, math.sqrt(c))
    # NaN值的一个特别的地方时它们之间的比较操作总是返回False
    print(c == d, c is d)


simple()
