# 需要使用路径名来获取文件名，目录名，绝对路径等等。
# 使用 os.path 模块中的函数来操作路径名。
import os

path = '/cookbook/fileio/print_file.py'
print(os.path.basename(path))
print(os.path.dirname(path))
# Join path components together
print(os.path.join('tmp','data',os.path.basename(path)))
# Expand the user's home directory
path = '~/Data/data.csv'
print(os.path.expanduser(path))
# Split the file extension
print(os.path.splitext(path))
# 对于任何的文件名的操作，你都应该使用 os.path 模块，而不是使用标准字符串
# 操作来构造自己的代码。特别是为了可移植性考虑的时候更应如此，因为 os.path 模
# 块知道 Unix 和 Windows 系统之间的差异并且能够可靠地处理类似 Data/data.csv 和
# Datandata.csv 这样的文件名
