import math as m


def l(x):
    return m.sqrt(1 + 2.5 * m.exp(2.5 * x))


def trapezio(a, b, h):
    n = round(abs((a - b) / h))
    total = 0
    for i in range(1, n):
        total += 2 * l(a + i * h)
    total += l(a) + l(b)

    total *= h / 2
    return total


def simpson(a, b, h):
    n = round(abs(a - b) / h)
    total = 0
    for i in range(1, n, 2):
        total += 4 * l(a + i * h)
    for i in range(2, n, 2):
        total += 2 * l(a + i * h)
    total += l(a) + l(b)
    total *= h / 3
    return total


r1 = trapezio(0, 1, 0.125)
r2 = trapezio(0, 1, 0.125 / 2)
r3 = trapezio(0, 1, 0.125 / 4)
quociente = (r2 - r1) / (r3 - r2)
erro = (r3 - r2) / 3
print("R1 = %.5f || R2 = %.5f || R3 = %.5f || QUOCIENTE = %.5f || ERRO = %.5f" % (r1, r2, r3, quociente, erro))

r1 = simpson(0, 1, 0.125)
r2 = simpson(0, 1, 0.125 / 2)
r3 = simpson(0, 1, 0.125 / 4)
quociente = (r2 - r1) / (r3 - r2)
erro = (r3 - r2) / 3
print("R1 = %.5f || R2 = %.5f || R3 = %.5f || QUOCIENTE = %.5f || ERRO = %.5f" % (r1, r2, r3, quociente, erro))
