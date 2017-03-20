# 你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定的
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re

print(re.split(r'[;,\s]\s*', line))
# 当你使用 re.split() 函数时候，需要特别注意的是正则表达式中是否包含一个括
# 号捕获分组。如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中。比如，
# 观察一下这段代码运行后的结果
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
# 获取分割字符在某些情况下也是有用的。比如，你可能想保留分割字符串，用来在
# 后面重新构造一个新的输出字符串
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values, delimiters)
print(''.join(v + d for v, d in zip(values, delimiters)))
# 如果你不想保留分割字符串到结果列表中去，但仍然需要使用到括号来分组正则表
# 达式的话，确保你的分组是非捕获分组，形如 (?:...)
items = re.split(r'(?:;|,|\s)\s*', line)
print(items)
