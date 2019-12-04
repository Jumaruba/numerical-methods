import math as m 

def f(x):
    return m.sin(x)/x*x


def trapezio(a,b,n):
    h = abs(a-b)/n
    total = 0
    for i in range(1,n):
        total += 2*f(a+i*h)
    total += f(a)+ f(b)
    total *= h/2
    return total

r1 = trapezio(m.pi/2, m.pi, 4)
r2 = trapezio(m.pi/2, m.pi, 4*2)
r3 = trapezio(m.pi/2, m.pi, 4*4)

quociente = (r2-r1)/(r3-r2) #precisa ser aproximadamente 4
print(quociente)
error = (r3-r2)/3
print(error)

#no teste de simpson, de facto é preciso dar o h
def simpson(a,b,h):
    n = round(abs(a-b)/h)
    total = 0
    for i in range(1,n,2):
        total += 4*f(a+i*h)
    for i in range(2,n,2):
        total += 2*f(a+i*h)
        
    total += f(a)+f(b)
    total*= h/3
    return total 

r1 = simpson(m.pi/2, m.pi, m.pi/8)
r2 = simpson(m.pi/2, m.pi, m.pi/16)
r3 = simpson(m.pi/2, m.pi, m.pi/32)


quociente = (r2-r1)/(r3-r2) #precisa ser aproximadamente 16
print(quociente)

error = (r3 - r2)/15
print(error)