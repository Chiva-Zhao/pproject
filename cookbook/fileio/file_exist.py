# 想测试一个文件或目录是否存在。
# 使用 os.path 模块来测试一个文件或目录是否存在。比如：
import os

print(os.path.exists('/etc/passwd'))
print(os.path.exists('file_exist.py'))
print(os.path.isfile('file_exist.py'))
print(os.path.isdir('file_exist.py'))
# Is a symbolic link
print(os.path.islink('file_exist.py'))
print(os.path.realpath('file_exist.py'))
# 如果你还想获取元数据 (比如文件大小或者是修改日期)，也可以使用 os.path 模块来解决
print(os.path.getsize('file_exist.py'))
print(os.path.getmtime('file_exist.py'))
import time

print(time.ctime(os.path.getmtime('file_exist.py')))
# 使用 os.path 来进行文件测试是很简单的。在写这些脚本时，可能唯一需要注意
# 的就是你需要考虑文件权限的问题，特别是在获取元数据时候
