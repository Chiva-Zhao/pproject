# 字符串的 I/O 操作
# 使用操作类文件对象的程序来操作文本或二进制字符串
# 使用 io.StringIO() 和 io.BytesIO() 类来创建类文件对象操作字符串数据。
import io

s = io.StringIO()
s.write('hello,world\n')
print('this is test', file=s)
# Get all of the data written so far
print(s.getvalue())
# Wrap a file interface around an existing string
s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())
# io.StringIO 只能用于文本。如果你要操作二进制数据，要使用 io.BytesIO 类来代替
s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())