def y_l(x,y):
    return x*x+y*y

def Euler(x,y,a,b,h):
    while (x< b-0.001):                  #atencao a isto
        x_anterior = x
        x = x_anterior+h
        y = y+h*y_l(x_anterior,y)
    print("x:",x)
    return y


#Calculando o erro
h = 0.1

r1 = Euler(0,0,0,1.4,0.1)
r2 = Euler(0,0,0,1.4,0.1/2)
r3 = Euler(0,0,0,1.4,0.1/4)
r4 = Euler(0,0,0,1.4,0.1/8)

print("y1:",r1)
print("y2:",r2)
print("y3:",r3)
quociente = (r3 - r2)/(r4-r3)           #o passo é adequado, quociente igual a 2(ou quase)
erro = (r4-r3)
print("quociente", quociente) 
print("erro:", erro)
