# 你需要转换或者输出使用二进制，八进制或十六进制表示的整数
x = 1234


def base():
    print(bin(x), oct(x), hex(x))
    print(format(x, 'b'), format(x, 'o'), format(x, 'x'))
    print(int('4d2', 16), int('10011010010', 2))


def chmod():
    import os
    os.chmod('num_format.py',0o755)

base()
chmod()
