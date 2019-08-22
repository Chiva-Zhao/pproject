def genfun():
    for i in range(10):
        yield i
for item in genfun():
    print(item)
print(next(genfun()))
mystr="hello,world"
# next(mystr)
myite=iter(mystr)
for item in myite:
    print(item)