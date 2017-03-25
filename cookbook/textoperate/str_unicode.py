# 你正在处理 Unicode 字符串，需要确保所有字符串在底层有相同的表示
import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'


def simple():
    print(s1, s2)
    print(s1 == s2)
    print(len(s1), len(s2))


# normalize() 第一个参数指定字符串标准化的方式。 NFC 表示字符应该是整体组
# 成 (比如可能的话就使用单一编码)，而 NFD 表示字符应该分解为多个组合字符表示
def advance():
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    print(t1 == t2)
    print(t1, ascii(t1))
    t3 = unicodedata.normalize('NFD', s1)
    t4 = unicodedata.normalize('NFD', s2)
    print(t3 == t4)
    print(ascii(t3))


# Python 同样支持扩展的标准化形式 NFKC 和 NFKD，它们在处理某些字符的时候
# 增加了额外的兼容特性
def more():
    s = '\ufb01'  # A single character
    print(s)
    print(unicodedata.normalize('NFD', s))
    print(unicodedata.normalize('NFKD', s))
    print(unicodedata.normalize('NFKC', s))
    # 最后一个例子展示了unicodedata模块的另一个重要方面，也就是测试字符类的
    # 工具函数。 combining()函数可以测试一个字符是否为和音字符。在这个模块中还有
    # 其他函数用于查找字符类别，测试是否为数字字符等等
    t1 = unicodedata.normalize('NFD', s1)
    t2 = ''.join(c for c in t1 if not unicodedata.combining(c))
    print(t1, t2)


more()
