# 排列组合的迭代
# 你想迭代遍历一个集合中元素的所有可能的排列或组合
items = ['a', 'b', 'c']
from itertools import permutations, combinations, combinations_with_replacement

for x in permutations(items):
    print(x)
for x in permutations(items, 2):
    print(x)
for x in combinations(items, 3):
    print(x)
for x in combinations(items, 2):
    print(x)
for x in combinations(items, 1):
    print(x)
for x in combinations_with_replacement(items, 3):
    print(x)
