# 打印不合法的文件名
# 你的程序获取了一个目录中的文件名列表，但是当它试着去打印文件名的时候程
# 序崩溃，出现了 UnicodeEncodeError 异常和一条奇怪的消息—— surrogates not allowed
# 当打印未知的文件名时，使用下面的方法可以避免这样的错误
import os


def bad_filename(filename):
    return repr(filename)[1:-1]


try:
    print('filename')
except UnicodeEncodeError:
    print(bad_filename('filename'))
print(list(fname for fname in os.listdir('.') if fname.endswith('txt')))
files = os.listdir('.')
for file in files:
    if file.endswith('txt'):
        print(file)
