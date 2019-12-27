import math as m


def f(x, y):
    return m.sin(y) + y * y / 4 + m.cos(x) + x * x / 4 - 1


def dfx(x, y):
    return x / 2 - m.sin(x)


def dfy(x, y):
    return m.cos(y) + y / 2


def dfxx(x, y):
    return 1 / 2 - m.cos(x)


def dfyy(x, y):
    return 1 / 2 - m.sin(y)


def dfxy(x, y):
    return 0


def dfyx(x, y):
    return 0


def quadratica(xn, yn):
    for i in range(30):
        det = dfyy(xn, yn) * dfxx(xn, yn) - dfyx(xn, yn) * dfxy(xn, yn)
        x = xn - (dfyy(xn, yn) * dfx(xn, yn) - dfyx(xn, yn) * dfx(xn, yn)) / det
        y = yn - (-dfxy(xn, yn) * dfx(xn, yn) + dfxx(xn, yn) * dfy(xn, yn)) / det
        xn = x
        yn = y
    return [x, y]


print(quadratica(0, 0))
