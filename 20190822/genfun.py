def genfun():
    for i in range(10):
        yield i


for item in genfun():
    print(item)
print(next(genfun()))
mystr = "hello,world"
# next(mystr)
myite = iter(mystr)
for item in myite:
    print(item)


def fabo(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for i in fabo(5):
    print(i)
