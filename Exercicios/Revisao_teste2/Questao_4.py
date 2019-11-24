import math as m

def yl(x,y):
    return 4*m.exp(0.8*x)-0.5*y

def euler(a,b,x,y,h):
    while (x < b -0.001):
        x_ant = x
        y_ant = y
        x = x_ant + h
        y = y_ant + h*yl(x_ant, y_ant)
    return y

r1 = euler(0,4,0,2,1)
r2 = euler(0,4,0,2,1/2)
r3 = euler(0,4,0,2,1/4)

quociente = (r2-r1)/(r3-r2)
erro = (r3-r2)

print("r1=", r1)
print("quociente", quociente)
print("erro", erro)

def rk2(a,b,x,y,h):
    while(x < b -0.001):
        x_ant = x
        y_ant = y
        x = x_ant + h
        y = y_ant + h*yl(x_ant + h/2, y_ant + h/2*yl(x_ant, y_ant))
    return y


r1 = rk2(0,4,0,2,1/4)
r2 = rk2(0,4,0,2,1/8)
r3 = rk2(0,4,0,2,1/16)

quociente = (r2-r1)/(r3-r2)
erro = (r3-r2)/3

print("r1=", r1)
print("quociente", quociente)
print("erro", erro)
