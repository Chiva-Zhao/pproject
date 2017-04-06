# 创建数据处理管道
# 生成器函数是一个实现管道机制的好办法
import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    '''Find all filenames in a directory tree that match a shell wildcard pattern'''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    '''Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.'''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    '''Chain a sequence of iterators together into a single sequence.'''
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    '''Look for a regex pattern in a sequence of lines'''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


# 现在你可以很容易的将这些函数连起来创建一个处理管道。比如，为了查找包含单
# 词 python 的所有日志行，你可以这样做
lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)
# 计算出传输的字节数并计算其总和
lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
bytes = (int(x) for x in bytecolumn if x != '-')
print('Total', sum(bytes))
