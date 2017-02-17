import numpy as np
import scipy.stats as stats
import scipy.optimize as opt

print(np.version.full_version)
rv_unif = stats.uniform.rvs(size=10)
print(rv_unif)
rv_beta = stats.beta.rvs(size=10, a=4, b=2)
print(rv_beta)

np.random.seed(seed=2015)
rv_beta = stats.beta.rvs(size=10, a=4, b=2)
print("method 1:")
print(rv_beta)

np.random.seed(seed=2015)
beta = stats.beta(a=4, b=2)
print("method 2:")
print(beta.rvs(size=10))

norm_dist = stats.norm(loc=0.5, scale=2)
n = 200
dat = norm_dist.rvs(size=n)
print("mean of data is: " + str(np.mean(dat)))
print("median of data is: " + str(np.median(dat)))
print("standard deviation of data is: " + str(np.std(dat)))

mu = np.mean(dat)
sigma = np.std(dat)
stat_val, p_val = stats.kstest(dat, 'norm', (mu, sigma))
print('KS-statistic D = %6.3f p-value = %6.4f' % (stat_val, p_val))
stat_val, p_val = stats.ttest_1samp(dat, 0)
print('One-sample t-statistic D = %6.3f, p-value = %6.4f' % (stat_val, p_val))

norm_dist2 = stats.norm(loc=-0.2, scale=1.2)
dat2 = norm_dist2.rvs(size=50)
stat_val, p_val = stats.ttest_ind(dat, dat2, equal_var=False)
print('Two-sample t-statistic D = %6.3f, p-value = %6.4f' % (stat_val, p_val))

g_dist = stats.gamma(a=2)
print("quantiles of 2, 4 and 5:")
print(g_dist.cdf([2, 4, 5]))
print("Values of 25%, 50% and 90%:")
print(g_dist.pdf([0.25, 0.5, 0.95]))
print(stats.norm.moment(6, loc=0, scale=1))

norm_dist = stats.norm(loc=0, scale=1.8)
dat = norm_dist.rvs(size=int(n / 2))
info = stats.describe(dat)
print(info)
print("Data size is: " + str(info[0]))
print("Minimum value is: " + str(info[1][0]))
print("Maximum value is: " + str(info[1][1]))
print("Arithmetic mean is: " + str(info[2]))
print("Unbiased variance is: " + str(info[3]))
print("Biased skewness is: " + str(info[4]))
print("Biased kurtosis is: " + str(info[5]))

norm_dist = stats.norm(loc=0, scale=1.8)
dat = norm_dist.rvs(size=100)
mu, sigma = stats.norm.fit(dat)
print("MLE of data mean:" + str(mu))
print("MLE of data standard deviation:" + str(sigma))

norm_dist = stats.norm()
dat1 = norm_dist.rvs(size=100)
exp_dist = stats.expon()
dat2 = exp_dist.rvs(size=100)
cor, pval = stats.pearsonr(dat1, dat2)
print("Pearson correlation coefficient: " + str(cor))
cor, pval = stats.spearmanr(dat1, dat2)
print("Spearman's rank correlation coefficient: " + str(cor))

x = stats.chi2.rvs(3, size=50)
y = 2.5 + 1.2 * x + stats.norm.rvs(size=50, loc=0, scale=1.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("Slope of fitted model is:", slope)
print("Intercept of fitted model is:", intercept)
print("R-squared:", r_value ** 2)


def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0)


x_0 = np.array([0.5, 1.6, 1.1, 0.8, 1.2])
res = opt.minimize(rosen, x_0, method='nelder-mead', options={'xtol': 1e-8, 'disp': True})
print("Result of minimizing Rosenbrock function via Nelder-Mead Simplex algorithm:")
print(res)


def rosen_der(x):
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    der = np.zeros_like(x)
    der[1:-1] = 200 * (xm - xm_m1 ** 2) - 400 * (xm_p1 - xm ** 2) * xm - 2 * (1 - xm)
    der[0] = -400 * x[0] * (x[1] - x[0] ** 2) - 2 * (1 - x[0])
    der[-1] = 200 * (x[-1] - x[-2] ** 2)
    return der


res = opt.minimize(rosen, x_0, method='BFGS', jac=rosen_der, options={'disp': True})
print("Result of minimizing Rosenbrock function via Broyden-Fletcher-Goldfarb-Shanno algorithm:")
print(res)


def rosen_hess(x):
    x = np.asarray(x)
    H = np.diag(-400 * x[:-1], 1) - np.diag(400 * x[:-1], -1)
    diagonal = np.zeros_like(x)
    diagonal[0] = 1200 * x[0] ** 2 - 400 * x[1] + 2
    diagonal[-1] = 200
    diagonal[1:-1] = 202 + 1200 * x[1:-1] ** 2 - 400 * x[2:]
    H = H + np.diag(diagonal)
    return H


res = opt.minimize(rosen, x_0, method='Newton-CG', jac=rosen_der, hess=rosen_hess, options={'xtol': 1e-8, 'disp': True})
print("Result of minimizing Rosenbrock function via Newton-Conjugate-Gradient algorithm (Hessian):")
print(res)


def rosen_hess_p(x, p):
    x = np.asarray(x)
    Hp = np.zeros_like(x)
    Hp[0] = (1200 * x[0] ** 2 - 400 * x[1] + 2) * p[0] - 400 * x[0] * p[1]
    Hp[1:-1] = -400 * x[:-2] * p[:-2] + (202 + 1200 * x[1:-1] ** 2 - 400 * x[2:]) * p[1:-1] \
               - 400 * x[1:-1] * p[2:]
    Hp[-1] = -400 * x[-2] * p[-2] + 200 * p[-1]
    return Hp


res = opt.minimize(rosen, x_0, method='Newton-CG', jac=rosen_der, hessp=rosen_hess_p,
                   options={'xtol': 1e-8, 'disp': True})
print(
    "Result of minimizing Rosenbrock function via Newton-Conjugate-Gradient algorithm (Hessian times arbitrary vector):")
print(res)


def func(x, sign=1.0):
    """ Objective function """
    return sign * (2 * x[0] * x[1] + 2 * x[0] - x[0] ** 2 - 2 * x[1] ** 2)


def func_deriv(x, sign=1.0):
    """ Derivative of objective function """
    dfdx0 = sign * (-2 * x[0] + 2 * x[1] + 2)
    dfdx1 = sign * (2 * x[0] - 4 * x[1])
    return np.array([dfdx0, dfdx1])


cons = (
    {'type': 'eq', 'fun': lambda x: np.array([x[0] ** 3 - x[1]]),
     'jac': lambda x: np.array([3.0 * (x[0] ** 2.0), -1.0])},
    {'type': 'ineq', 'fun': lambda x: np.array([x[1] - 1]), 'jac': lambda x: np.array([0.0, 1.0])})

res = opt.minimize(func, [-1.0, 1.0], args=(-1.0,), jac=func_deriv, method='SLSQP', options={'disp': True})
print("Result of unconstrained optimization:")
print(res)
res = opt.minimize(func, [-1.0, 1.0], args=(-1.0,), jac=func_deriv, constraints=cons, method='SLSQP',
                   options={'disp': True})
print("Result of constrained optimization:")
print(res)
