from functools import reduce

product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)
