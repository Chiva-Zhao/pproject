from numpy import array, tensordot

T = array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
    [[21, 22, 23], [24, 25, 26], [27, 28, 29]]])
print(T.shape)
# define first tensor
A = array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
    [[21, 22, 23], [24, 25, 26], [27, 28, 29]]])
# define second tensor
B = array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
    [[21, 22, 23], [24, 25, 26], [27, 28, 29]]])
C = A + B
print(A + B)
print(A - B)
print(A * B)
print(A / B)

# tensor product
A = array([1, 2])
B = array([3, 4])
print(tensordot(A, B, axes=0))

A = array([[1, 2],
           [3, 4]])
B = array([[2, 3],
           [4, 5]])
print(tensordot(A, B, 0))
