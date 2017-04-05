# 跳过可迭代对象的开始部分
# 你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们
from itertools import dropwhile, islice

with open('somefile.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 2, None):
    print(x)

for x in islice(items, None, 3):
    print(x)
# 本节的方案适用于所有可迭代对象，包括那些事先不能确定大小的，比如生成器，文件及其类似的对象