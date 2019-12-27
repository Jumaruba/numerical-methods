import math as m


def f(x, y):
    return y * y - 2 * x * y - 6 * y + 2 * x * x + 12


def dfx(x, y):
    return 4 * x - 2 * y


def dfy(x, y):
    return 2 * y - 2 * x - 6


def gradiente(x_ant, y_ant, h):
    for i in range(30):
        x = x_ant - h * dfx(x_ant, y_ant)
        y = y_ant - h * dfy(x_ant, y_ant)
        if f(x, y) < f(x_ant, y_ant):
            h = 2 * h
            y_ant = y
            x_ant = x
        if f(x, y) > f(x_ant, y_ant):
            h = h / 2
        print(x_ant, y_ant)


gradiente(1,1,1)
