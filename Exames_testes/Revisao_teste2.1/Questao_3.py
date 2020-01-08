import math as m 

def f(x):
    return 1 - m.exp(-x)

def trapezio(a,b,n):
    h = (abs(a-b)/n)
    total = 0
    for i in range(1,n):
        total += 2*f(a+i*h)
    total += f(a) + f(b)
    return total

print(trapezio(0,4,4))
r1 = trapezio(0,4,4) 
r2 = trapezio(0,4,4*2)
r3 = trapezio(0,4,4*4)

quociente = (r2 - r1)/(r3 - r2)
print("quociente_trapezio:", quociente) #precisa ser aproximadamente 4
erro = (r3 -r2)/3
print("error:", erro)  


def simpson(a,b,n): 
    h = (abs(a-b)/n)
    total = 0
    for i in range(1,n,2): #todos os impares
        total += 4*f(a+i*h) 
    for i in range(2,n,2): #todos os pares
        total += 2*f(a+i*h)
    total += f(a)+f(b)
    total *= h/3
    return total

print("simpson:", simpson(0,4,4))
r1 = simpson(0,4,4)
r2 = simpson(0,4,4*2)
r3 = simpson(0,4,4*4)
quociente = (r2 - r1)/(r3-r2)
erro = (r3-r2)/15
print("quociente_simpson:", quociente)  #precisa ser aproximadamente 16
print("erro_simpson", erro)

# o passo é adequado
# caso nao fosse continuarimaos a dobrar o n até que satisfazesse as condições
