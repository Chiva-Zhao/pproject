# basic
from numpy import array, empty, zeros, ones

a = [1.0, 2, 4]
arr = array(a)
print(arr)
print(arr.shape, arr.dtype)

em = empty([3, 3])
print(em)
print(em.shape)

zeo = zeros([3, 5])
print(zeo)
print(zeo.shape)

one = ones([2, 4])
print(one, one.shape)
# combine array
from numpy import vstack, hstack

a1 = array([1, 2, 3])
a2 = array([[4, 5, 6],
            [7, 8, 9]])
a12 = vstack((a1, a2))
print(a12, a12.shape)

a3 = array([[1, 2], [3, 4]])
a23 = hstack((a3, a2))
print(a23, a23.shape)
