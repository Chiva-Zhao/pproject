foo = ['hi']
print(foo)
# Output: ['hi']
bar = foo
bar += ['bye']
print(foo)


def add_to(num, target=[]):
    target.append(num)
    return target


print(add_to(1))
print(add_to(2))


def add_to2(num, target=None):
    if target is None:
        target = []
    target.append(num)
    return target


print(add_to2(1))
print(add_to2(2))
