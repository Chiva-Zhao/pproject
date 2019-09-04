from numpy import array
from matplotlib import pyplot

# define dataset
data = array([
    [0.05, 0.12],
    [0.18, 0.22],
    [0.31, 0.35],
    [0.42, 0.38],
    [0.5, 0.49]])
# pyplot.plot(data)
# pyplot.show()
# split into inputs and outputs
x, y = data[:, 0], data[:, 1]
x = x.reshape((len(x), 1))
# scatter plot
pyplot.scatter(x, y)
pyplot.show()
