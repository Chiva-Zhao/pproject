# 你想使用 Unix Shell 中常用的通配符 (比如 *.py , Dat[0-9]*.csv 等) 去匹配文本字符串
# fnmatch 模块提供了两个函数—— fnmatch() 和 fnmatchcase() ，可以用来实现这样的匹配
from fnmatch import fnmatch, fnmatchcase

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]


def default():
    print(fnmatch('foo.txt', '*.txt'))
    print(fnmatch('foo.txt', '?oo.txt'))
    print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
    print([name for name in names if fnmatch(name, '*.csv')])
    print(fnmatchcase('foo.txt', '*.TXT'))


# 这两个函数通常会被忽略的一个特性是在处理非文件名的字符串时候它们也是很有用的
def advance():
    print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
    print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])


advance()
