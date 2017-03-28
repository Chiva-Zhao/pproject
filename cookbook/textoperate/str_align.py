# 字符串对齐
# 对于基本的字符串对齐操作，可以使用字符串的 ljust() , rjust() 和 center()方法

text = "Hello world"


def basic():
    print(text.ljust(20), text.ljust(20, '='))
    print(text.rjust(20), text.rjust(20, '-'))
    print(text.center(20), text.center(20, '*'))


# 函数 format() 同样可以用来很容易的对齐字符串。你要做的就是使用 <,> 或者
# ˆ 字符后面紧跟一个指定的宽度
def format_ex():
    print(format(text, '<20'), format(text, '=<20'))
    print(format(text, '>20'), format(text, '->20'))
    print(format(text, '^20'), format(text, '*^20'))
    print('{:>10} {:>10}'.format('hello', 'world'))
    x = 1.2345
    print(format(x, '>10'), format(x, '^10.2f'))
    print('%-20s' % text)
    print('%20s' % text)


# basic()
format_ex()
