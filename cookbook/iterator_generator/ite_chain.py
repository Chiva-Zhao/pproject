# 不同集合上元素的迭代
# 你想在多个对象执行相同的操作，但是这些对象在不同的容器中，你希望代码在不
# 失可读性的情况下避免写重复的循环
# itertools.chain() 方法可以用来简化这个任务。它接受一个可迭代对象列表作为
# 输入，并返回一个迭代器，有效的屏蔽掉在多个容器中迭代细节
from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)
# Inefficent
for x in a + b:
    pass
# Better
for x in chain(a, b):
    pass
# 第一种方案中， a + b 操作会创建一个全新的序列并要求 a 和 b 的类型一致。
# chian() 不会有这一步，所以如果输入序列非常大的时候会很省内存。并且当可迭代
# 对象类型不一样的时候 chain() 同样可以很好的工作