import math as m 

def f(x): 
    return m.sin(x)

def trapezio(a,b,n):
    h = abs((a-b)/n)
    total = 0
    for i in range(1,n):
        total += 2*f(a+i*h)

    total+= f(a)+f(a+n*h)
    total*=h/2

    print(total)

trapezio(0,m.pi,10)
