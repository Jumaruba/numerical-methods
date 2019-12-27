import math as m


def f(x, y):
    return y * y - 2 * x * y - 6 * y + 2 * x * x + 12


def dfx(x, y):
    return 4 * x - 2 * y


def dfy(x, y):
    return 2 * y - 2 * x - 6


def gradiente(xn, yn, h):
    for i in range(30):
        x = xn - h * dfx(xn, yn)
        y = yn - h * dfy(xn, yn)
        if f(x, y) < f(xn, yn):
            h *= 2
            xn = x
            yn = y
        else:
            h /= 2
    return [x, y]


print(gradiente(1, 1, 1))
#Expected result: 
#[2.9765625, 5.984375]
