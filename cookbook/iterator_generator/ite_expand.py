# 展开嵌套的序列
# 你想将一个多层嵌套的序列展开成一个单层列表
# 可以写一个包含 yield from 语句的递归生成器来轻松解决这个问题
from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            # yield from flatten(x)
            for i in flatten(x):
                yield i
    else:
        yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x)
items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)
