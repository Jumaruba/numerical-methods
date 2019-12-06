import math as m 

def f(x): 
    return m.sin(x)/(x*x)


def simpson(a,b,h):
    total = 0
    n = round(abs((b-a)/h))
    for i in range(1,n,2):  #odd values
        total += 4*f(a+i*h)
    for i in range(2,n,2):  #even values 
        total+= 2*f(a+i*h)

    total+= f(a)+f(a+n*h)   #get the first value and last value
    total *= h/3

    return total 

# Calculo da convergencia
print(simpson(m.pi/2, m.pi, m.pi/8))

r1 = simpson(m.pi/2, m.pi, m.pi/8)
r2 = simpson(m.pi/2, m.pi, m.pi/16)
r3 = simpson(m.pi/2, m.pi, m.pi/32)
r4 = simpson(m.pi/2, m.pi, m.pi/64)

coeficiente = (r3-r2)/(r4-r3)

print("r1:",r1)
print("r2:",r2)
print("r3", r3)
print("coeficiente:", coeficiente)

# Calculo do erro
erro = (r4-r3)/15
print("erro:", abs(erro)) # erros sempre em modulo 