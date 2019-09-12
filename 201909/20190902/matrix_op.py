from numpy import array, trace, rank
from numpy.linalg import inv, det, matrix_rank

A = array([
    [1, 2],
    [3, 4],
    [5, 6]])
print(A.T)
# matrix inv
A = array([
    [1.0, 2.0],
    [3.0, 4.0]])
B = inv(A)
print(B)
print(A.dot(B))
# matrix trace
A = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
print(trace(A))
# matrix Determinant
print(det(A))
# rank
print(matrix_rank(A))
v1 = array([1, 2, 3])
vr1 = matrix_rank(v1)
print(vr1)
# zero rank
v2 = array([0, 0, 0, 0, 0])
print(matrix_rank(v2))

# rank 0
M0 = array([
    [0, 0],
    [0, 0]])
print(M0)
mr0 = matrix_rank(M0)
print(mr0)
# rank 1
M1 = array([
    [1, 2],
    [1, 2]])
print(M1)
mr1 = matrix_rank(M1)
print(mr1)
# rank 2
M2 = array([
    [1, 2],
    [3, 4]])
print(M2)
mr2 = matrix_rank(M2)
print(mr2)
