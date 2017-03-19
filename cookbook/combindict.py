# 合并多个字典或映射
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}


def default():
    c = ChainMap(a, b)
    print(len(c), list(c.keys()), list(c.values()))
    print(c['x'], c['y'], c['z'])


# ChainMap 对于编程语言中的作用范围变量 (比如 globals , locals 等) 是非常有用的
def more():
    values = ChainMap()
    values['x'] = 1
    print(values)
    values = values.new_child()
    values['x'] = 2
    print(values)
    values = values.new_child()
    values['x'] = 3
    print(values, values['x'], values.parents['x'], values.parents.parents['x'])


# 作为 ChainMap 的替代，你可能会考虑使用 update() 方法将两个字典合并
def update():
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    merged = dict(b)
    merged.update(a)
    print(merged['x'], merged['y'], merged['z'])
    a['x'] = 13
    print(merged)

    # ChainMap使用原来的字典，它自己不创建新的字典。所以它并不会产生上面所说的结果
    merged = ChainMap(a, b)
    print(merged)
    a['x'] = 42
    print(merged)


update()
