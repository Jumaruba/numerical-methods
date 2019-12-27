import math as m


def f(x):
    return (2 * x + 1) ** 2 - 5 * m.cos(10 * x)


def aurea_max(x1, x2):
    b = (m.sqrt(5) - 1) / 2
    a = b * b
    for i in range(30):
        x3 = x1 + a * (x2 - x1)
        x4 = x1 + b * (x2 - x1)
        if f(x3) > f(x4):
            x2 = x4
            x4 = x3
        else:
            x1 = x3
            x3 = x4
    return [x1, x2, x3, x4]


def aurea_min(x1, x2):
    b = (m.sqrt(5) - 1) / 2
    a = b * b
    for i in range(30):
        x3 = x1 + a * (x2 - x1)
        x4 = x1 + b * (x2 - x1)
        if f(x3) < f(x4):
            x2 = x4
            x4 = x3
        else:
            x1 = x3
            x3 = x4
    return [x1, x2, x3, x4]


print(aurea_max(-1, 0))
#Expected result:
#[-0.31113734222759837, -0.3111368047370985, -0.311137136924496, -0.311137136924496]
print(aurea_min(-1, 0))
#Expected result: 
#[-0.6262978964093815, -0.6262973589188816, -0.6262976911062791, -0.6262976911062791]