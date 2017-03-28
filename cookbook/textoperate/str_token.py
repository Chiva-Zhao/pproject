# 字符串令牌解析
import re
from collections import namedtuple

text = 'foo = 23 + 42 * 10'

# tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
# ('NUM', '42'), ('TIMES', '*'), ('NUM', 10')]

# ?P<TOKENNAME> 用于给一个模式命名，供后面使用
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))


def simple():
    # 下一步，为了令牌化，使用模式对象很少被人知道的scanner()方法。这个方法
    # 会创建一个scanner对象，在这个对象上不断的调用match()方法会一步步的扫描目
    # 标文本，每步一个匹配
    scanner = master_pat.scanner('foo=42')
    _ = scanner.match()
    print(_.lastgroup, _.group())
    _ = scanner.match()
    print(_.lastgroup, _.group())
    _ = scanner.match()
    print(_.lastgroup, _.group())


def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


# Example use
# for tok in generate_tokens(master_pat, 'foo = 42'):
    # print(tok)
# Produces output
# Token(type='NAME', value='foo')
# Token(type='WS', value=' ')
# Token(type='EQ', value='=')
# Token(type='WS', value=' ')
# Token(type='NUM', value='42')
# 如果你想过滤令牌流，你可以定义更多的生成器函数或者使用一个生成器表达式。
# 比如，下面演示怎样过滤所有的空白令牌：
tokens = (tok for tok in generate_tokens(master_pat, text)
          if tok.type != 'WS')
# for tok in tokens:
#     print(tok)
PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
master_pat = re.compile('|'.join([PRINT, NAME]))
for tok in generate_tokens(master_pat, 'printer'):
    print(tok)
# simple()
