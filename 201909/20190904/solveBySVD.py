# The Singular-Value Decomposition, or SVD for short, is a matrix decomposition method like
# the QR decomposition.
# X = U · Σ · V T
# Where A is the real  m x n matrix that we wish to decompose, U is a m × m matrix, Σ (often
# represented by the uppercase Greek letter Sigma) is an m × n diagonal matrix, and V T is the
# transpose of an n × n matrix. Unlike the QR decomposition, all matrices have a singular-value
# decomposition. As a basis for solving the system of linear equations for linear regression, SVD
# is more stable and the preferred approach. Once decomposed, the coefficients can be found by
# calculating the pseudoinverse of the input matrix X and multiplying that by the output vector
# y.
# b = X+ · y
# Where the pseudoinverse X+ is calculated as following:
# X+ = U · D+ · V T

# SVD solution via pseudoinverse to linear least squares
from numpy import array
from numpy.linalg import pinv
from matplotlib import pyplot

# define dataset
data = array([
    [0.05, 0.12],
    [0.18, 0.22],
    [0.31, 0.35],
    [0.42, 0.38],
    [0.5, 0.49]])
# split into inputs and outputs
X, y = data[:, 0], data[:, 1]
X = X.reshape((len(X), 1))
# calculate coefficients
b = pinv(X).dot(y)
print(b)
# predict using coefficients
yhat = X.dot(b)
# plot data and predictions
pyplot.scatter(X, y)
pyplot.plot(X, yhat, color='red')
pyplot.show()
