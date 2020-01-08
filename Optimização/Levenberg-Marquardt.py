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


def dfyx(x, y):
    return -2


def dfxy(x, y):
    return -2


# xn+1  xn - invert(hessiana).gradient + lambda.gradiente
def levenberg(x, y, lamb):
    x_ant = x
    y_ant = y
    for i in range(20):
        det = dfxx(x_ant, y_ant) * dfyy(x_ant, y_ant) - dfxy(x_ant, y_ant) * dfyx(x_ant, y_ant)
        x = x_ant - (dfyy(x_ant, y_ant) * dfx(x_ant, y_ant) - dfxy(x_ant, y_ant) * dfy(x_ant, y_ant)) / det - lamb * (

            dfx(x_ant, y_ant))
        y = y_ant - (-dfxy(x_ant, y_ant) * dfx(x_ant, y_ant) + dfxx(x_ant, y_ant) * dfy(x_ant, y_ant)) / det - lamb * dfy(x_ant, y_ant)
        if f(x_ant, y_ant) > f(x,y):
            lamb/=2 
        else: 
            lamb*=2
        x_ant = x 
        y_ant = y
        print(x, y)
    return [x, y]


r = levenberg(1, 1, 0.1)
print(f(r[0], r[1]))


