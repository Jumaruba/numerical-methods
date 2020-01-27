

def dft(T):
    return -0.25*(T - 59)


def euler(T,t):
    for _ in range(3): 
        print(t,T)
        T = T + 0.5*dft(T)
        t += 0.5


euler(2,2)