# 迭代器代替 while 无限循环
CHUNKSIZE = 8192


def process_data(data):
    pass


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


# 这种代码通常可以使用 iter() 来代替
def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        pass
        # process_data(data)


import sys

f = open('somefile.txt')
for chunk in iter(lambda: f.read(10), '\n'):
    print(sys.stdout.write(chunk))
# iter 函数一个鲜为人知的特性是它接受一个可选的 callable 对象和一个标记 (结
# 尾) 值作为输入参数。当以这种方式使用的时候，它会创建一个迭代器，这个迭代器会
# 不断调用 callable 对象直到返回值和标记值相等为止。
# 这种特殊的方法对于一些特定的会被重复调用的函数很有效果，比如涉及到 I/O
# 调用的函数。举例来讲，如果你想从套接字或文件中以数据块的方式读取数据，通常
# 你得要不断重复的执行 read() 或 recv() ，并在后面紧跟一个文件结尾测试来决定是
# 否终止。这节中的方案使用一个简单的 iter() 调用就可以将两者结合起来了。其中
# lambda 函数参数是为了创建一个无参的 callable 对象，并为 recv 或 read() 方法提
# 供了 size 参数。