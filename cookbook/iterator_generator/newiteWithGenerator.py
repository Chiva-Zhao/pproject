# 使用生成器创建新的迭代模式
# 如果你想实现一种新的迭代模式，使用一个生成器函数来定义它
def frange(start, end, step):
    x = start
    while x < end:
        yield x
        x += step


# 为了使用这个函数，你可以用 for 循环迭代它或者使用其他接受一个可迭代对象的
# 函数 (比如 sum() , list() 等)
for n in frange(0, 4, 0.5):
    print(n)
print(list(frange(0, 1, 0.125)))
print(sum(frange(0, 5, 1)))


# 一个函数中需要有一个 yield 语句即可将其转换为一个生成器。跟普通函数不同
# 的是，生成器只能用于迭代操作
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')


c = countdown(3)
print(c)
# Run to first yield and emit a value
print(next(c),next(c))
print(next(c),next(c))
# 一个生成器函数主要特征是它只会回应在迭代中使用到的 next 操作。一旦生成器
# 函数返回退出，迭代终止。我们在迭代中通常使用的 for 语句会自动处理这些细节，所
# 以你无需担心
