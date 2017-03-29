# 执行精确的浮点数运算
a = 4.2
b = 2.1


def basic():
    print(a + b, a + b == 6.3)


def use_decimal():
    from decimal import Decimal
    a = Decimal('4.2')
    b = Decimal('2.1')
    print(a + b, a + b == Decimal('6.3'))
    # decimal模块的一个主要特征是允许你控制计算的每一方面，包括数字位数和四舍
    # 五入运算。为了这样做，你先得创建一个本地上下文并更改它的设置
    from decimal import localcontext
    a = Decimal('1.3')
    b = Decimal('1.7')
    print(a / b)
    with localcontext() as ctx:
        ctx.prec = 3
        print(a / b)
    with localcontext() as ctx:
        ctx.prec = 50
        print(a / b)
    nums = [1.23e+18, 1, -1.23e+18]
    print(sum(nums))  # Notice how 1 disappears
    # 上面的错误可以利用math.fsum()所提供的更精确计算能力来解决
    import math
    print(math.fsum(nums))


# basic()
use_decimal()
