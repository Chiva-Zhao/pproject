some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
dup = []
for some in some_list:
    if some_list.count(some) > 1:
        if some not in dup:
            dup.append(some)
print(dup)

dup1 = set([x for x in some_list if some_list.count(x) > 1])
print(dup1)
# 交集
valid = {'yellow', 'red', 'blue', 'green', 'black'}
input_set = {'red', 'brown'}
# print(valid.intersection(input_set))
print(input_set.difference(valid))

valid = {'yellow', 'red', 'blue', 'green', 'black'}
input_set = {'red', 'brown'}
print(input_set.difference(valid))