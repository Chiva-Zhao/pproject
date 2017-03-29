# 字节字符串上的字符串操作
def basic():
    data = b'Hello World'
    print(data[0:5], data.startswith(b'Hello'), data.replace(b'Hello', b'Hello Cruel'), sep='\n')
    data = bytearray(b'Hello World')
    print(data[0:5], data.startswith(b'Hello'), data.replace(b'Hello', b'Hello Cruel'), sep='\n')
    # 你可以使用正则表达式匹配字节字符串，但是正则表达式本身必须也是字节串
    data = b'FOO:BAR,SPAM'
    import re
    print(re.split(b'[:,]', data))


def more():
    a = 'Hello World'  # Text string
    print(a[0], a[1])
    b = b'Hello World'  # Byte string
    print(b[0], b[1])
    s = b'Hello World'
    print(s)
    print(s.decode('ascii'))
    print(b'%10s %10d %10.2f' % (b'ACME', 100, 490.1))
    # print(b'{} {} {}'.format(b'ACME', 100, 490.1))
    print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))


# basic()
more()
