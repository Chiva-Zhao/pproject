# 数字的四舍五入
# 对于简单的舍入运算，使用内置的 round(value, ndigits) 函数即可
def simple():
    print(round(1.23, 1))
    print(round(1.27, 1))
    print(round(-1.27, 1))
    print(round(1.25361, 3))
    # 传给 round() 函数的 ndigits 参数可以是负数，这种情况下，舍入运算会作用在 十位、百位、千位等上面
    a = 1627731
    print(round(a, -1), round(a, -2), round(a, -3))
    x = 1.23456
    print(format(x, '0.2f'), format(x, '0.3f'), 'value is {:0.3f}'.format(x))


simple()
