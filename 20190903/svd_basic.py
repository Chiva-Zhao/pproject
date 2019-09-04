from numpy import array, zeros, diag
from numpy.linalg import inv, svd, pinv
# The Singular-Value Decomposition, or SVD for short, is a matrix decomposition method for
# reducing a matrix to its constituent parts in order to make certain subsequent matrix calculations
# simpler. For the case of simplicity we will focus on the SVD for real-valued matrices and ignore
# the case for complex numbers.
# A = U · Σ · V T
# Where A is the real m × n matrix that we wish to decompose, U is an m × m matrix, Σ
# represented by the uppercase Greek letter sigma) is an m × n diagonal matrix, and V T is the V
# transpose of an n × n matrix where T is a superscript
A = array([
    [1, 2],
    [3, 4],
    [5, 6]])
u, s, v = svd(A)
print(u)
print(s)
print(v)
# reconstruct rectangular matrix from svd
# create m x n Sigma matrix
sigma = zeros((A.shape[0], A.shape[1]))
# populate Sigma with n x n diagonal matrix
sigma[:A.shape[1], :A.shape[1]] = diag(s)
# reconstruct matrix
B = u.dot(sigma.dot(v))
print(B)

A = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
u, s, v = svd(A)
print(u, s, v)
B = u.dot(diag(s).dot(v))
print(B)

# pseudoinverse
# The pseudoinverse is denoted as A+, where A is the matrix that is being inverted and + is a
# superscript. The pseudoinverse is calculated using the singular value decomposition of A:
# A+ = V · D+ · UT
# Where A+ is the pseudoinverse, D+ is the pseudoinverse of the diagonal matrix Σ and V T is
# the transpose of V T . We can get U and V from the SVD operation.
# A = U · Σ · V T
# The D+ can be calculated by creating a diagonal matrix from Σ, calculating the reciprocal
# of each non-zero element in Σ, and taking the transpose if the original matrix was rectangular.
# The specific implementation is: A+ = V T · DT · UT
A = array([
    [0.1, 0.2],
    [0.3, 0.4],
    [0.5, 0.6],
    [0.7, 0.8]])
print(pinv(A))
# pseudoinverse via svd
u, s, v = svd(A)
d = zeros(A.shape)
d[:A.shape[1], :A.shape[1]] = diag(1 / s)
# calculate pseudoinverse
B = v.T.dot(d.T.dot(u.T))
print(B)

# Dimensionality Reduction
# A popular application of SVD is for dimensionality reduction. Data with a large number of
# features, such as more features (columns) than observations (rows) may be reduced to a smaller
# subset of features that are most relevant to the prediction problem. The result is a matrix with
# a lower rank that is said to approximate the original matrix. To do this we can perform an SVD
# operation on the original data and select the top k largest singular values in Σ. These columns
# can be selected from Σ and the rows selected from V T . An approximate B of the original vector
# A can then be reconstructed.
# B = U · Σk · VkT
A = array([
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]])
u, s, v = svd(A)
# create m x n Sigma matrix
sigma = zeros(A.shape)
# populate Sigma with n x n diagonal matrix
sigma[:A.shape[0], :A.shape[0]] = diag(s)
# select
k = 2
sigma = sigma[:, :k]
v = v[:k, :]
# reconstruct
B = u.dot(sigma.dot(v))
print(B)
# transform
T = u.dot(sigma)
print(T)
T = A.dot(v.T)
print(T)

# svd data reduction in scikit-learn
# The scikit-learn provides a TruncatedSVD class that implements this capability directly. The
# TruncatedSVD class can be created in which you must specify the number of desirable features
# or components to select, e.g. 2. Once created, you can fit the transform (e.g. calculate VkT )
# by calling the fit() function, then apply it to the original matrix by calling the transform()
# function. The result is the transform of A called T above. The example below demonstrates the
# TruncatedSVD class
from sklearn.decomposition import TruncatedSVD

A = array([
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]])
# create transform
svd = TruncatedSVD(2)
# fit transform
svd.fit(A)
# apply transform
result = svd.transform(A)
print(result)

