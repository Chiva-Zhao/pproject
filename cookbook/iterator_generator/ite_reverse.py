# 反向迭代
# 使用内置的 reversed() 函数，比如
a = [1, 2, 3, 4]
for i in reversed(a):
    print(i)


# 可以通过在自定义类上实现 reversed () 方法来实现反向迭代
class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

# 定义一个反向迭代器可以使得代码非常的高效，因为它不再需要将数据填充到一个
# 列表中然后再去反向迭代这个列表
for rr in reversed(Countdown(30)):
    print(rr)
for rr in Countdown(30):
    print(rr)
