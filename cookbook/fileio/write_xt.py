# 向一个文件中写入数据，但是前提必须是这个文件在文件系统上不存在。也就
# 是不允许覆盖已存在的文件内容
# 可以在 open() 函数中使用 x 模式来代替 w 模式的方法来解决这个问题
# 如果文件是二进制的，使用 xb 来代替 xt
# with open('somefile', 'wt') as f:
#     f.write('Hello\n')
# with open('somefile', 'xt') as f:
#     f.write('Hello\n')
# 这一小节演示了在写文件时通常会遇到的一个问题的完美解决方案 (不小心覆盖一
# 个已存在的文件)。一个替代方案是先测试这个文件是否存在
import os

if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')
