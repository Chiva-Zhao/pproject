# 你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀， URL Scheme 等等
def common():
    # 检 查 字 符 串 开 头 或 结 尾 的 一 个 简 单 方 法 是 使 用 str.startswith() 或 者 是str.endswith() 方法
    filename = "test.txt"
    print(filename.startswith("hello"))
    print(filename.endswith("txt"))

    # 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传给 startswith() 或者 endswith() 方法
    import os
    filenames = os.listdir(".")
    print(filenames)
    corpy = [name for name in filenames if name.endswith(('.c', '.py'))]
    print(corpy)
    print(any(name.endswith('py') for name in filenames))


from urllib.request import urlopen


# 奇怪的是，这个方法中必须要输入一个元组作为参数。如果你恰巧有一个 list 或
# 者 set 类型的选择项，要确保传递参数前先调用 tuple() 将其转换为元组类型。
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


def slice():
    # startswith() 和 endswith() 方法提供了一个非常方便的方式去做字符串开头和
    # 结尾的检查。类似的操作也可以使用切片来实现，但是代码看起来没有那么优雅。
    filename = 'spam.txt'
    print(filename[-4:] == '.txt')
    url = 'http://www.python.org'
    url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'


def regex():
    import re
    url = "http://www.python.org"
    re.match("http:|https:|ftp:", url)
    # 最后提一下，当和其他操作比如普通数据聚合相结合的时候startswith()和endswith()
    # 方法是很不错的。比如，下面这个语句检查某个文件夹中是否存在指定的文件类型
    # if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
