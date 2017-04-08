# 需要读写各种不同编码的文本数据，比如 ASCII， UTF-8 或 UTF-16 编码等
# 使用带有 rt 模式的 open() 函数读取文本文件
# Read the entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()
print(data)
# Iterate over the lines of the file
with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line)
        # process line
# 类似的，为了写入一个文本文件，使用带有 wt 模式的 open() 函数，如果之前文
# 件内容存在则清除并覆盖掉
# Write chunks of text data
with open('somefile.txt', 'wt') as f:
    f.write('text1')
    f.write('text2')
# Redirected print statement
with open('somefile.txt', 'wt') as f:
    print('line1', file=f)
    print('line2', file=f)
# 如果是在已存在文件中添加内容，使用模式为 at 的 open() 函数。
# 文件的读写操作默认使用系统编码，可以通过调用 sys.getdefaultencoding() 来
# 得到。在大多数机器上面都是 utf-8 编码。如果你已经知道你要读写的文本是其他编码
# 方式，那么可以通过传递一个可选的 encoding 参数给 open() 函数
with open('somefile.txt', 'rt', encoding='latin-1') as f:
    pass
# Replace bad chars with Unicode U+fffd replacement char
f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
f.read()
# Ignore bad chars entirely
g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
g.read()
