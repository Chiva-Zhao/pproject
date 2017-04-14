# 读写二进制数组数据
# 可以使用 struct 模块处理二进制数据。下面是一段示例代码将一个 Python 元组
# 列表写入一个二进制文件，并使用 struct 将每个元组编码为一个结构体
from struct import Struct


def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


# Example
if __name__ == '__main__':
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]
    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)


# 有很多种方法来读取这个文件并返回一个元组列表。首先，如果你打算以块的形式
# 增量读取文件，你可以这样做
def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


# Example
if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            print(rec)


# 如果你想将整个文件一次性读取到一个字节字符串中，然后在分片解析。那么你可以这样做
def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))


# Example
if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        data = f.read()
    for rec in unpack_records('<idd', data):
        print(rec)
# 两种情况下的结果都是一个可返回用来创建该文件的原始元组的可迭代对象。
# 结构体通常会使用一些结构码值 i, d, f 等 [参考 Python 文档 ]。这些代码分别代表
# 某个特定的二进制数据类型如 32 位整数， 64 位浮点数， 32 位浮点数等。第一个字符
# < 指定了字节顺序。在这个例子中，它表示” 低位在前”。更改这个字符为 > 表示高位
# 在前，或者是 ! 表示网络字节顺序。
# 产生的 Struct 实例有很多属性和方法用来操作相应类型的结构。 size 属性包含
# 了结构的字节数，这在 I/O 操作时非常有用。 pack() 和 unpack() 方法被用来打包和
# 解包数据
from struct import Struct

record_struct = Struct('<idd')
print(record_struct.size)
print(record_struct.pack(1, 2.0, 3.0))
print(record_struct.unpack(record_struct.pack(1, 2.0, 3.0)))
# 有时候你还会看到 pack() 和 unpack() 操作以模块级别函数被调用
import struct

print(struct.pack('<idd', 1, 2.0, 3.0))
print(struct.unpack('<idd', struct.pack('<idd', 1, 2.0, 3.0)))
# 读取二进制结构的代码要用到一些非常有趣而优美的编程技巧。在函数　
# read records 中， iter() 被用来创建一个返回固定大小数据块的迭代器
# 这个迭代器会不断的调用一个用户提供的可调用对象 (比如 lambda:
# f.read(record struct.size) )，直到它返回一个特殊的值 (如 b’‘)，这时候迭代停止
f = open('data.b', 'rb')
chunks = iter(lambda: f.read(20), b'')
print(chunks)
for chk in chunks:
    print(chk)
# 如你所见，创建一个可迭代对象的一个原因是它能允许使用一个生成器推导来创建记录

# 在 函 数 unpack records() 中 使 用 了 另 外 一 种 方 法 unpack from() 。
# unpack from() 对于从一个大型二进制数组中提取二进制数据非常有用，因为它不
# 会产生任何的临时对象或者进行内存复制操作。你只需要给它一个字节字符串 (或数
# 组) 和一个字节偏移量，它会从那个位置开始直接解包数据

# 在解包的时候， collections 模块中的命名元组对象或许是你想要用到的。它可以
# 让你给返回元组设置属性名称
from collections import namedtuple

Record = namedtuple('Record', ['kind', 'x', 'y'])
with open('data.b', 'rb') as f:
    records = (Record(*r) for r in read_records('<idd', f))
for r1 in records:
    print(r1.kind, r1.x, r1.y)
# 如果你的程序需要处理大量的二进制数据，你最好使用 numpy 模块。例如，你可以
# 将一个二进制数据读取到一个结构化数组中而不是一个元组列表中

import numpy as np

f = open('data.b', 'rb')
records = np.fromfile(f, dtype='<i,<d,<d')
print(records)
# 最后提一点，如果你需要从已知的文件格式 (如图片格式，图形文件， HDF5 等)
# 中读取二进制数据时，先检查看看 Python 是不是已经提供了现存的模块
