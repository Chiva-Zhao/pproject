# 实现自定义容器
import bisect
import collections


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)


items = SortedItems([5, 1, 3])
print(list(items))
print(items[0], items[-1])
items.add(2)
print(list(items))
# 可以看到， SortedItems 跟普通的序列没什么两样，支持所有常用操作，包括索引、
# 迭代、包含判断，甚至是切片操作。
# 这里面使用到了 bisect 模块，它是一个在排序列表中插入元素的高效方式。可以
# 保证元素插入后还保持顺序
# 使用 collections 中的抽象基类可以确保你自定义的容器实现了所有必要的方法。
# 并且还能简化类型检查。你的自定义容器会满足大部分类型检查需要

items = SortedItems()
print(isinstance(items, collections.Iterable))
print(isinstance(items, collections.Sequence))
print(isinstance(items, collections.Container))
print(isinstance(items, collections.Sized))
print(isinstance(items, collections.Mapping))


# collections 中 很 多 抽 象 类 会 为 一 些 常 见 容 器 操 作 提 供 默 认 的 实 现， 这
# 样 一 来 你 只 需 要 实 现 那 些 你 最 感 兴 趣 的 方 法 即 可。 假 设 你 的 类 继 承 自
# collections.MutableSequence ，如下
class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)


# 如果你创建 Items 的实例，你会发现它支持几乎所有的核心列表方法 (如 append()、
# remove()、 count() 等)。下面是使用演示：
a = Items([1, 2, 3])
print(len(a))
print(a.append(4))
print(a.append(2))
print(a.count(2))
print(a.remove(3))
