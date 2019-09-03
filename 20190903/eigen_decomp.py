# Eigendecomposition of a matrix is a type of decomposition that involves decomposing a square
# matrix into a set of eigenvectors and eigenvalues
# A vector is an eigenvector of a matrix if it satisfies the following equation. A · v = λ · v
from numpy import array, diag
from numpy.linalg import eig, inv

A = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
values, vectors = eig(A)
print(values)
print(vectors)
# confirm first eigenvector
print(A.dot(vectors[:, 0]))
print(values[0] * vectors[:, 0])
print(A.dot(vectors[:, 1]))
print(values[1] * vectors[:, 1])
print(A.dot(vectors[:, 2]))
print(values[2] * vectors[:, 2])
# Reconstruct Matrix
B = vectors.dot(diag(values)).dot(inv(vectors))
print(B)
