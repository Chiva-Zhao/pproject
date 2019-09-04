from numpy import array
from numpy.linalg import qr, cholesky
from scipy.linalg import lu

# The LU decomposition is for square matrices and decomposes a matrix into L and U components
A = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
P, L, U = lu(A)
print(P)
print(L)
print(U)
B = P.dot(L).dot(U)
print(B)
# The QR decomposition is for n × m matrices (not limited to square matrices) and decomposes
# a matrix into Q and R components.
# A = Q · R
A = array([
    [1, 2],
    [3, 4],
    [5, 6]])

# Q, R = qr(A)
Q, R = qr(A, 'complete')
print(Q)
print(R)
print(Q.dot(R))
# Cholesky Decomposition A = L · LT
# The Cholesky decomposition is for square symmetric matrices where all values are greater than
# zero, so-called positive definite matrices
A = array([
    [2, 1, 1],
    [1, 2, 1],
    [1, 1, 2]])
L = cholesky(A)
print(L)
print(L.T)
print(L.dot(L.T))
