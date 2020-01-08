import math as m 

def f(x): 
    return m.sin(x)

def simpson(a,b,n):
    h = abs((a-b)/n)
    total = 0
    for i in range(1,n,2):
        total+= 4*f(a+i*h)
    for i in range(2,n,2):
        total+= 2*f(a+i*h)
    
    total+= f(a)+f(a+n*h)
    total*= h/3
    print(total)

simpson(0,m.pi/2,10)
