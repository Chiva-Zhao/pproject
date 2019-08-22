items = [1, 2, 3, 4, 5]
squred = []
for item in items:
    squred.append(item ** 2)
print(squred)

squred1 = list(map(lambda x: x ** 2, items))
print(squred1)


def multi(x):
    return x * x


def add(x):
    return x + x


funcs = [multi, add]
for i in range(5):
    print(list(map(lambda x: x(i), funcs)))
