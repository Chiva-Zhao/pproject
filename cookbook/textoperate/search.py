# 你想匹配或者搜索特定模式的文本
import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'


def simple():
    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text == 'yeah')
    print(text.startswith('yeah'))
    print(text.endswith('bug'))
    print(text.find('no'))


def re_match():
    if re.match(r'\d+/\d+/\d+', text1):
        print('yes')
    else:
        print('no')
    if re.match(r'\d+/\d+/\d+', text2):
        print('yes')
    else:
        print('no')


def re_match1():
    datepat = re.compile(r'\d+/\d+/\d+')
    if datepat.match(text1):
        print('yes')
    else:
        print('no')
    if datepat.match(text2):
        print('yes')
    else:
        print('no')
    print(datepat.findall(text))
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = datepat.match('03/21/2017')
    print(m, m.group(0), m.group(1), m.group(2), m.group(3), m.groups())
    month, day, year = m.groups()
    print(month, day, year)
    for month, day, year in datepat.findall(text):
        print("{}-{}-{}".format(year, month, day))
    for m in datepat.finditer(text):
        print(m.groups())


# simple()
# re_match()
re_match1()
