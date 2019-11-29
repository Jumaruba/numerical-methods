import math as m 


def f_(t,y):
    return 4*m.exp(0.8*t) - 0.5*y


def euler(a,b,tn_1, yn_1, h): 
    while (tn_1 < b -0.001): 
        tn = tn_1
        yn = yn_1
        tn_1 = tn + h
        yn_1 = yn + h*f_(tn, yn)
    return [tn_1, yn_1]

r1 = euler(0,4,0,2,1)[1]
r2 = euler(0,4,0,2,1/2)[1]
r3 = euler(0,4,0,2,1/4)[1]

quociente = (r2 - r1)/(r3 - r2)
print("r1 =", r1)
print("quociente_euler =", quociente)   # passo adequado

def runga_kutta(a,b,x,y,h):
    while (x < b -0.001):
        x_ant = x 
        x = x_ant + h
        y = y + h*f_(x_ant + h/2, y + h/2*f_(x_ant,y))
    return y

r1 = runga_kutta(0,4,0,2,1/4)
r2 = runga_kutta(0,4,0,2,1/8)
r3 = runga_kutta(0,4,0,2,1/16)

quociente = (r2 - r1)/(r3 - r2)

print("r1 =",r1)
print("quociente_runga=", quociente)    #precisa ser proximo de 4
