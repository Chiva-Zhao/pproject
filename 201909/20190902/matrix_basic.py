from numpy import array

A = array([[1, 2, 3], [4, 5, 6]])
B = array([
    [1, 2, 3],
    [4, 5, 6]])
print(A + B)
B = array([
    [0.5, 0.5, 0.5],
    [0.5, 0.5, 0.5]])
print(A - B)
print(A * B)
print(A / B)

A = array([
    [1, 2],
    [3, 4],
    [5, 6]])
B = array([
    [1, 2],
    [3, 4]])
print(A.dot(B))
print(A @ B)

B = array([0.5, 0.5])
print(A.dot(B))

# matrix-scalar multiplication
b = 0.5
print(A * b)
# triangular matrices
from numpy import tril, triu, diag, identity

M = array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]])
print(tril(M))
print(triu(M))
print(diag(M))
print(diag(diag(M)))
print(identity(3))
# Orthogonal Matrix
from numpy.linalg import inv

Q = array([
    [1, 0],
    [0, -1]])
V = inv(Q)
print(Q)
print(Q.T)
I = Q.dot((Q.T))
print(I)
