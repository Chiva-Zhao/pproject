# 忽略文件名编码
# 默认情况下，所有的文件名都会根据 sys.getfilesystemencoding() 返回的文本
# 编码来编码或解码
# 如果因为某种原因你想忽略这种编码，可以使用一个原始字节字符串来指定一个文件名即可

# Wrte a file using a unicode filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')
import os

print(list(fname for fname in os.listdir('.') if fname.endswith('txt')))
print(list(fname for fname in os.listdir(b'.') if fname.endswith(b'txt')))
# Open file with raw filename
with open(b'jalape\xc3\xb1o.txt') as f:
    print(f.read())
# 通常来讲，你不需要担心文件名的编码和解码，普通的文件名操作应该就没问题
# 了。但是，有些操作系统允许用户通过偶然或恶意方式去创建名字不符合默认编码的
# 文件。这些文件名可能会中断那些需要处理大量文件的 Python 程序。
# 读取目录并通过原始未解码方式处理文件名可以有效的避免这样的问题，尽管这样
# 会带来一定的编程难度