# 增加或改变已打开文件的编码
# 想在不关闭一个已打开的文件前提下增加或改变它的 Unicode 编码。
# 如果想给一个以二进制模式打开的文件添加 Unicode 编码/解码方式，可以使用
# io.TextIOWrapper() 对象包装它
import urllib.request
import io

# u = urllib.request.urlopen('http://www.python.org')
# f = io.TextIOWrapper(u, encoding='utf-8')
# text = f.read()
# 如果你想修改一个已经打开的文本模式的文件的编码方式，可以先使用 detach()
# 方法移除掉已存在的文本编码层，并使用新的编码方式代替
import sys

print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)
f = open('somefile.txt', 'w')
print(f)
print(f.buffer)
print(f.buffer.raw)
# 在这个例子中， io.TextIOWrapper 是一个编码和解码 Unicode 的文本处理层，
# io.BufferedWriter 是一个处理二进制数据的带缓冲的 I/O 层， io.FileIO 是一个表
# 示操作系统底层文件描述符的原始文件。增加或改变文本编码会涉及增加或改变最上
# 面的 io.TextIOWrapper 层

# detach() 方法会断开文件的最顶层并返回第二层，之后最顶层就没什么用了
f = open('sample.txt', 'w')
print(f)
b = f.detach()
print(b)
# f.write("hello,world")
# 一旦断开最顶层后，你就可以给返回结果添加一个新的最顶层
f = io.TextIOWrapper(b, encoding='latin-1')
print(f)
# 尽管已经向你演示了改变编码的方法，但是你还可以利用这种技术来改变文件行处
# 理、错误机制以及文件处理的其他方面
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii',
                              errors='xmlcharrefreplace')
print('Jalape\u00f1o')
# Jalape&#241;o
# 注意下最后输出中的非 ASCII 字符 ñ 是如何被 &#241; 取代的
