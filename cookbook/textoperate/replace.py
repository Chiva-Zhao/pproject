# 你想在字符串中搜索和替换指定的文本模式
def simple():
    text = 'yeah, but no, but yeah, but no, but yeah'
    replaced = text.replace('yeah', 'yap')
    print(text, replaced)


import re

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'


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

re_match()
print(datepat.sub(re_more, text))
