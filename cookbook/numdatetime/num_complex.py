# 复数的数学运算
import cmath

a = complex(5, 7)
b = 6 + 9j


def simple():
    print(a, b)
    print(a.real, a.imag, a.conjugate())
    print(a + b, a - b, a * b, a / b, abs(a))


def cmath_demo():
    print(cmath.sin(a), cmath.cos(a), cmath.exp(a))


def numpy_demo():
    import numpy as np
    a = np.array([2 + 3j, 4 + 5j, 6 - 7j, 8 + 9j])
    print(a, a + 2, np.sin(a))
    print(cmath.sqrt(-1))


# cmath_demo()
numpy_demo()
