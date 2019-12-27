import math as m


def f(x, y):
    return y * y - 2 * x * y - 6 * y + 2 * x * x + 12


def dfx(x, y):
    return 4 * x - 2 * y


def dfy(x, y):
    return 2 * y - 2 * x - 6


def dfxx(x, y):
    return 4


def dfyy(x, y):
    return 2


def dfxy(x, y):
    return -2


def dfyx(x, y):
    return -2


def levemberg(xn, yn, lamb):
    for i in range(20):
        det = dfyy(xn, yn) * dfxx(xn, yn) - dfyx(xn, yn) * dfxy(xn, yn)
        x = xn - (dfyy(xn, yn) * dfx(xn, yn) - dfyx(xn, yn) * dfy(xn, yn)) / det - lamb * dfx(xn, yn)
        y = yn - (-dfxy(xn, yn) * dfx(xn, yn) + dfxx(xn, yn) * dfy(xn, yn)) / det - lamb * dfy(xn, yn)
        if (x - xn <= 0) and (y - yn <= 0):
            xn = x
            yn = y
        lamb /= 2
    return [x, y]


print(levemberg(1, 1, 1))
#Expected result [2.9999961853027344, 6.000011444091797]
