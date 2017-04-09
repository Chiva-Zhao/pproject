# 获取文件系统中某个目录下的所有文件列表。
# 使用 os.listdir() 函数来获取某个目录中的文件列表：
import os

print(os.listdir('.'))
# 结果会返回目录中所有文件列表，包括所有文件，子目录，符号链接等等。如果你
# 需要通过某种方式过滤数据，可以考虑结合 os.path 库中的一些函数来使用列表推导
import os.path

# Get all regular files
names = [name for name in os.listdir('.')
         if os.path.isfile(os.path.join('.', name))]
print(names)
# Get all dirs
dirnames = [name for name in os.listdir('.')
            if os.path.isdir(os.path.join('.', name))]
print(dirnames)
# 字符串的 startswith() 和 endswith() 方法对于过滤一个目录的内容也是很有用的
pyfiles = [name for name in os.listdir('.')
           if name.endswith('.py')]
print(pyfiles)
# 对于文件名的匹配，你可能会考虑使用 glob 或 fnmatch 模块
import glob
from fnmatch import fnmatch

pyfiles = glob.glob('./*.py')
print(pyfiles)
pyfiles = [name for name in os.listdir('.')
           if fnmatch(name, '*.py')]
print(pyfiles)
# 获取目录中的列表是很容易的，但是其返回结果只是目录中实体名列表而已。如
# 果你还想获取其他的元信息，比如文件大小，修改时间等等，你或许还需要使用到
# os.path 模块中的函数或着 os.stat() 函数来收集数据
# Example of getting a directory listing
import os
import os.path
import glob

pyfiles = glob.glob('*.py')
# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]
for name, size, mtime in name_sz_date:
    print(name, size, mtime)
# Alternative: Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
