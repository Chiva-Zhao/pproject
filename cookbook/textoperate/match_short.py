# 你正在试着用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹
# 配。而你想修改它变成查找最短的可能匹配
import re


def common():
    str_pat = re.compile(r'\"(.*)\"')
    text1 = 'Computer says "no."'
    print(str_pat.findall(text1))
    text2 = 'Computer says "no." Phone says "yes."'
    print(str_pat.findall(text2))
    # 在这个例子中，模式r'n"(.*)n"'的意图是匹配被双引号包含的文本。
    # 但是在正则表达式中 * 操作符是贪婪的，因此匹配操作会查找最长的可能匹配。于是在第二个
    # 例子中搜索text2的时候返回结果并不是我们想要的。
    # 为了修正这个问题，可以在模式中的 * 操作符后面加上? 修饰符
    # 这样就使得匹配变成非贪婪模式，从而得到最短的匹配，也就是我们想要的结果
    str_pat = re.compile(r'\"(.*?)\"')
    print(str_pat.findall(text2))


# 你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配
def multi_line():
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a comment */'
    text2 = '''/* this is a
    multiline comment */'''
    print(comment.findall(text1))
    # 为了修正这个问题，你可以修改模式字符串，增加对换行的支持
    print(comment.findall(text2))
    # 在这个模式中， (?:.|\n) 指定了一个非捕获组(也就是它定义了一个仅仅用来做
    # 匹配，而不能通过单独捕获或者编号的组)
    comment = re.compile(r'/\*((?:.|\n)*?)\*/')
    print(comment.findall(text2))
    # re.compile()函数接受一个标志参数叫re.DOTALL ，在这里非常有用。它可以让
    # 正则表达式中的点(.) 匹配包括换行符在内的任意字符
    comment = re.compile(r'/\*(.*?)\*/', flags=re.DOTALL)
    print(comment.findall(text2))

common()
multi_line()
