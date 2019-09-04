# Solve via Inverse
# The first approach is to attempt to solve the regression problem directly using the matrix inverse.
# That is, given X, what are the set of coefficients b that when multiplied by X will give y. As
# we saw in a previous section, the normal equations define how to calculate b directly.
# b = (XT · X)−1 · XT · y
from numpy import array
from numpy.linalg import inv
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
# linear least squares
b = inv(X.T.dot(X)).dot((X.T)).dot(y)
print(b)
# predict using coefficients
yhat = X.dot(b)
# plot data and predictions
pyplot.scatter(X, y)
pyplot.plot(X, yhat, color='red')
pyplot.show()
