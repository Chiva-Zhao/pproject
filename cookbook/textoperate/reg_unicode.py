# 在正则式中使用 Unicode
import re


def re_d():
    num = re.compile("\d+")
    print(num.match('234'))
    print(num.match('\u0661\u0662\u0663'))
    arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
    pat = re.compile('stra\u00dfe', re.IGNORECASE)
    s = 'straße'
    print(pat.match(s))
    print(pat.match(s.upper()))

re_d()
