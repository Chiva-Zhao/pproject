# 创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉
s = '{name} has {n} messages.'


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


def simple():
    print(s.format(name='Guido', n=37))
    # 或者，如果要被替换的变量能在变量域中找到，那么你可以结合使用 format map()和 vars()
    name = 'Chiva'
    n = 22
    print(s.format_map(vars()))
    a = Info('luoli', 37)
    print(s.format_map(vars(a)))
    # print(s.forat(name='hell'))
    name = 'lalalala'
    n = 37
    print('%(name) has %(n) messages.' % vars())


def more():
    import string
    s = string.Template('$name has $n messages.')
    name = 'lalalala'
    n = 37
    print(s.substitute(vars()))


# simple()
more()
