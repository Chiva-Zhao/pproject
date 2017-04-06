# 序列上索引值迭代
# 迭代一个序列的同时跟踪正在被处理的元素索引
from collections import defaultdict

mylist = ['a', 'b', 'c']
for idx, item in enumerate(mylist):
    print(idx, item)
for idx, item in enumerate(mylist, 1):
    print(idx, item)


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
        try:
            count = int(fields[1])
        except ValueError as e:
            print('Line {}: Parse error: {}'.format(lineno, e))


# 将一个文件中出现的单词映射到它出现的行号上去，可以很容易的利用 enumerate() 来完成
word_summary = defaultdict()
with open("somefile.txt", 'rt') as f:
    lines = f.readlines()
for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)
# 还有一点可能并不很重要，但是也值得注意，有时候当你在一个已经解压后的元组
# 序列上使用 enumerate() 函数时很容易调入陷阱。你得像下面正确的方式这样写
data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
# Correct!
# for n, (x, y) in enumerate(data):
# Error!
# for n, x, y in enumerate(data):