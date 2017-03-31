# 分数运算
from fractions import Fraction  # fractions 模块可以被用来执行包含分数的数学运算

a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b, a * b)
# Getting numerator/denominator
c = a + b
print(c.numerator, c.denominator, float(c))
# Limiting the denominator of a value
print(c.limit_denominator(8))
# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(x.as_integer_ratio(), y)
