from numpy import array

a = array([1, 2, 3])
b = 2
c = a + b
print(c)
# Scalar and Two-Dimensional Array
A = array([
    [1, 2, 3],
    [1, 2, 3]])
c = A + b
print(c)
# One-Dimensional and Two-Dimensional Arrays
b = array([1, 2, 3])
c = A + b
print(c)
# Limitations of Broadcasting
b = array([1, 2])
c = A + b #ValueError: operands could not be broadcast together with shapes (2,3) (2,)
