import math as m


def f(x):
    return x ** 3 - 10 * m.sin(x) + 2.8


def bissection(a, b):
    m = 0
    for i in range(3):
        print("%i || M = %.5f" % (i, m))
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return m


bissection(1.5, 4.2)
