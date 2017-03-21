# 你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
# 最简单的过滤序列元素的方法就是使用列表推导。比如：
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])
pos = (n for n in mylist if n > 0)
print(list(pos))

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


# 假设过滤的时候需要处理一些异常或者其他复杂情况。这时候你可以将过
# 滤代码放到一个函数中，然后使用内建的 filter() 函数
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)
# 过滤的时候转换数据
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math

print([math.sqrt(n) for n in mylist if n > 0])
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)

# itertools.compress()
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]  # 现在你想将那些对应 count 值大于 5 的地址全部输出
from itertools import compress

more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))
