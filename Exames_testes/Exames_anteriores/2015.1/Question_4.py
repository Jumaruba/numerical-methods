import math as m


def df(x):
    return 2 * m.log(2 * x)


def f(x):
    return m.exp(x) - 4 * x * x


def picard_peano(x):
    for i in range(10):
        print(" %i || X = %.5f" % (i, x))
        x = df(x)


picard_peano(1.1)
print("Resíduo da primeira iteração:", 1.1 - 1.57691)
