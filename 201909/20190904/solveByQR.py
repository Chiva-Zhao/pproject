# The QR decomposition is an approach of breaking a matrix down into its constituent elements.
# A = Q · R
# Where A is the matrix that we wish to decompose, Q a matrix with the size m × m, and R
# is an upper triangle matrix with the size m × n. The QR decomposition is a popular approach
# for solving the linear least squares equation. Stepping over all of the derivation, the coefficients
# can be found using the Q and R elements as follows:
# b = R−1 · QT · y
from numpy import array
from numpy.linalg import inv, qr
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
# factorize
Q, R = qr(X)
b = inv(R).dot(Q.T).dot(y)
print(b)
# predict using coefficients
yhat = X.dot(b)
# plot data and predictions
pyplot.scatter(X, y)
pyplot.plot(X, yhat, color='red')
pyplot.show()