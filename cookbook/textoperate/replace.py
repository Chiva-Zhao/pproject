import re

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'


# 你想在字符串中搜索和替换指定的文本模式
def simple():
    text = 'yeah, but no, but yeah, but no, but yeah'
    replaced = text.replace('yeah', 'yap')
    print(text, replaced)


# 对于复杂的模式，请使用 re 模块中的 sub() 函数。为了说明这个，假设你想将形
# 式为 11/27/2012 的日期字符串改成 2012-11-27
def re_match():
    replaced = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
    print(replaced)
    print(datepat.sub(r'\3-\1-\2', text))
    newtext, n = datepat.subn(r'\3-\1-\2', text)
    print(newtext, n)


# 对于更加复杂的替换，可以传递一个替换回调函数来代替
def re_more(m):
    from calendar import month_abbr
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


def ignoreCase():
    text = 'UPPER PYTHON, lower python, Mixed Python'
    print(re.findall("python", text, flags=re.IGNORECASE))
    print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
    # 最后的那个例子揭示了一个小缺陷，替换字符串并不会自动跟被匹配字符串的大小
    # 写保持一致。为了修复这个，你可能需要一个辅助函数
    print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))


# re_match()
# print(datepat.sub(re_more, text))
ignoreCase()
