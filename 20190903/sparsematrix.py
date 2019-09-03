from numpy import array,count_nonzero
from scipy.sparse import csr_matrix

# create dense matrix
A = array([
    [1, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 1],
    [0, 0, 0, 2, 0, 0]])
print(A)
S = csr_matrix(A)
print(S)
B = S.todense()
print(B)
sparsity = 1-count_nonzero(A)/A.size
print(sparsity)