import math as m 

def f(x): 
    return 1-m.exp(-x)

def trapezio(a,b,x,n):
    h = abs(a-b)/n
    total = 0
    for i in range(1,n):
        total += 2*f(a+i*h)
    total += f(a) + f(b)
    total*= h/2
    return total

r1 = trapezio(0,4,0,4)
r2 = trapezio(0,4,0,4*2)
r3 = trapezio(0,4,0,4*4)

quociente = (r2-r1)/(r3-r2)
erro = (r3-r2)/3
print("r1=", r1)
print("quociente=", quociente)
print("erro=", erro)

def simpson(a,b,x,n):
    h = abs(a-b)/n
    total = 0
    for i in range(1,n,2):
        total+= 4*f(a+i*h)
    for i in range(2,n,2):
        total+= 2*f(a+i*h)
    total += f(a) + f(b)
    total*= h/3
    return total

r1 = simpson(0,4,0,4)
r2 = simpson(0,4,0,4*2)
r3 = simpson(0,4,0,4*4)

quociente = (r2-r1)/(r3-r2)
erro = (r3-r2)/15
print("r1=", r1)
print("quociente=", quociente)
print("erro=", erro)