# 读写压缩文件
# gzip 和 bz2 模块可以很容易的处理这些文件。两个模块都为 open() 函数提供了
# 另外的实现来解决这个问题
import gzip
import bz2

# gzip compression
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)
# bz2 compression
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)
# 大部分情况下读写压缩数据都是很简单的。但是要注意的是选择一个正确的文件模
# 式是非常重要的。如果你不指定模式，那么默认的就是二进制模式，如果这时候程序
# 想要接受的是文本数据，那么就会出错。 gzip.open() 和 bz2.open() 接受跟内置的
# open() 函数一样的参数，包括 encoding， errors， newline 等等。
# 当写入压缩数据时，可以使用 compresslevel 这个可选的关键字参数来指定一个
# 压缩级别
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)
# 默认的等级是 9，也是最高的压缩等级。等级越低性能越好，但是数据压缩程度也越低。
# 最后一点， gzip.open() 和 bz2.open() 还有一个很少被知道的特性，它们可以作
# 用在一个已存在并以二进制模式打开的文件上。
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
# 这样就允许 gzip 和 bz2 模块可以工作在许多类文件对象上，比如套接字，管道和
# 内存中文件等。
