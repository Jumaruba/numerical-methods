import math as m


def dft(T):
    return -0.25 * (T - 37)


def euler(T, t, h):
    for i in range(3):
        print("%i || T = %.5f || t = %.5f" % (i, T, t))
        T += h * dft(T)
        t += h


euler(3, 5, 0.4)
