# vector mean
from numpy import array, mean, var, std, cov, corrcoef

v = array([1, 2, 3, 4, 5, 6])
print(mean(v))
# matrix means
M = array([
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]])
print(mean(M))
print(mean(M, axis=0))  # col_mean
print(mean(M, axis=1))  # row_mean

# vector variance
print(var(v, ddof=1))
# matrix variances
# column variances
col_var = var(M, ddof=1, axis=0)
print(col_var)
# row variances
row_var = var(M, ddof=1, axis=1)
print(row_var)
# column standard deviations
print(std(M, ddof=1, axis=0))
# row standard variances
print(std(M, ddof=1, axis=1))

# In probability, covariance is the measure of the joint probability for two random variables. It
# describes how the two variables change together. It is denoted as the function cov(X; Y ), where
# X and Y are the two random variables being considered.
# cov(X; Y )
# vector covariance
x = array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = array([9, 8, 7, 6, 5, 4, 3, 2, 1])
# calculate covariance
sigma = cov(x, y)[0, 1]
print(sigma)

# The covariance can be normalized to a score between -1 and 1 to make the magnitude
# interpretable by dividing it by the standard deviation of X and Y . The result is called the
# correlation of the variables, also called the Pearson correlation coefficient, named for the
# developer of the method.
# r =cov(X,Y)/sX × sY
print(cov(x,y)/(std(x)*std(y)))
print(corrcoef(x, y)[0, 1])

# define matrix of observations
X = array([
    [1, 5, 8],
    [3, 5, 11],
    [2, 4, 9],
    [3, 6, 10],
    [1, 5, 10]])
# calculate covariance matrix
Sigma = cov(X.T)
print(Sigma)
