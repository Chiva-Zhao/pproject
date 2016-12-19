from math import exp


def trapezoidal(f, a, b, n):
    period = float(b - a)
    step = period / n
    sum = 0.5 * f(a) + 0.5 * f(b)
    for i in range(1, n):
        sum += f(a + i * step)
    return step * sum


def application():
    v = lambda t: 3 * (t ** 2) * exp(t ** 3)
    n = int(input('n: '))
    numerical = trapezoidal(v, 0, 1, n)
    # Compare with exact result
    V = lambda t: exp(t ** 3)
    exact = V(1) - V(0)
    error = exact - numerical
    print('n=%d: %.16f, error: %g' % (n, numerical, error))


def midpoint(f, a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(n):
        x = a + i * h + h / 2
        sum += f(x)
    return sum * h


g = lambda y: exp(-y ** 2)
a = 0
b = 2
print(' n midpoint trapezoidal')
for i in range(1, 21):
    n = 2 ** i
    m = midpoint(g, a, b, n)
    t = trapezoidal(g, a, b, n)
    print('%7d %.16f %.16f' % (n, m, t))
