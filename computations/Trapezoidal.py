from math import exp


def trapezoidal(f, a, b, n):
    period = float(b - a)
    step = period / n
    sum = 0.5 * f(a) + 0.5 * f(b)
    for i in range(1, n):
        sum += f(a + i * step)
    return step * sum


def application():
    from math import exp
    v = lambda t: 3 * (t ** 2) * exp(t ** 3)
    n = int(input('n: '))
    numerical = trapezoidal(v, 0, 1, n)
    # Compare with exact result
    V = lambda t: exp(t ** 3)
    exact = V(1) - V(0)
    error = exact - numerical
    print('n=%d: %.16f, error: %g' % (n, numerical, error))


application()
