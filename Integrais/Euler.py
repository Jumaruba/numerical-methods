def y_l(x,y):
    return x*x+y*y

def Euler(x,y,a,b,h):
    while (x< b-0.01):                  #atencao a isto
        x_anterior = x
        x = x_anterior+h
        y = y+h*y_l(x_anterior,y)
    print("x:",x)
    return y

Euler(0,0,0,1.4,0.1)

#Calculando o erro
h = 0.1

r1 = Euler(0,0,0,1.4,0.1)
r2 = Euler(0,0,0,1.4,0.1/2)
r3 = Euler(0,0,0,1.4,0.1/4)
r4 = Euler(0,0,0,1.4, 0.0025/2)

print("y1:",r1)
print("y2:",r2)
print("y3:",r3)
quociente = (r2 - r1)/(r3-r2)           #o passo é adequado
erro = r3-r2
print("quociente", quociente) 
print("erro:", erro)
