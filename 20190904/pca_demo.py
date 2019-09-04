# Principal Component Analysis, or PCA for short, is a method for reducing the dimensionality
# of data. It can be thought of as a projection method where data with m-columns (features) is
# projected into a subspace with m or fewer columns, whilst retaining the essence of the original
# data
from numpy import array, mean, cov
from numpy.linalg import eig

A = array([
    [1, 2],
    [3, 4],
    [5, 6]])
# column means
M = mean(A, axis=0)
# center columns by subtracting column means
C = A - M
# calculate covariance matrix of centered matrix
V = cov(C.T)
# factorize covariance matrix
values, vectors = eig(V)
print(values)
print(vectors)
# project data
# P = vectors.T.dot(C.T)
# print(P.T)
P = C.dot(vectors)
print(P)

# Principal Component Analysis in scikit-learn
from sklearn.decomposition import PCA

# define matrix
A = array([
    [1, 2],
    [3, 4],
    [5, 6]])
pca = PCA(2)
# fit transform
pca.fit(A)
# access values and vectors
print(pca.components_)
print(pca.explained_variance_)
B = pca.transform(A)
print(B)
