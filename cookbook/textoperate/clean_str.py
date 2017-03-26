import unicodedata
import sys

# 审查清理文本字符串
s = 'pýtĥöñ\fis\tawesome\r\n'
remp = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
a = s.translate(remp)
print(a)


def trans():
    cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                             if unicodedata.combining((chr(c))))
    b = unicodedata.normalize('NFD', a)
    print(b)
    b = b.translate(cmb_chrs)
    print(b)


def more():
    digitmap = {c: ord('0') + unicodedata.digit(chr(c))
                for c in range(sys.maxunicode)
                if unicodedata.category(chr(c)) == 'Nd'}
    print(len(digitmap))
    x = '\u0661\u0662\u0663'
    print(x.translate(digitmap))


# 另一种清理文本的技术涉及到 I/O 解码与编码函数。这里的思路是先对文本做一
# 些初步的清理，然后再结合 encode() 或者 decode() 操作来清除或修改它
def decode():
    b = unicodedata.normalize('NFD', a)
    print(b)
    b = b.encode('ascii', 'ignore').decode('ascii')
    print(b)


# simple()
# trans()
# more()
decode()
