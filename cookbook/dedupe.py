# 删除重复元素，并保持其顺序
def dedupe(items):
    rst = set()
    for item in items:
        if item not in rst:
            yield item
            rst.add(item)
            # rst = {item for item in items if item not in rst}


def dedupe_dict(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe_dict(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe_dict(a, key=lambda d: d['x'])))
