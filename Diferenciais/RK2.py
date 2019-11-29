def y_l(x,y):
    return x*x+y*y

def runga_kutta(x,y,a,b,h):
    while (x < b-0.01): 
        x_anterior = x
        x = x_anterior + h
        y = y + h*y_l(x_anterior+h/2, y+h/2*y_l(x_anterior,y))

    print(x,y)
    return y

runga_kutta(0,0,0,1.4,1)

r1 = runga_kutta(0,0,0,1.4,0.1)
r2 = runga_kutta(0,0,0,1.4,0.1/2)
r3 = runga_kutta(0,0,0,1.4,0.1/4)

quociente = (r2-r1)/(r3-r2)
print("quociente = ", quociente)
erro = (r3-r2)/3
print("erro", erro)