import math as m

def f(x,y):
    return x**2+y**2

def runga_kutta(a,b,x,y,h):
    while (x < b-0.01):
        x_ant = x
        x = x_ant + h

        delta_1 = h*f(x_ant,y)
        delta_2 = h*f(x_ant + (h/2), y+ (delta_1/2))
        delta_3 = h*f(x_ant + (h/2), y + (delta_2/2))
        delta_4 = h*f(x_ant + h, y + delta_3)
        y = y + (delta_1/6) + (delta_2/3) + (delta_3/3) + (delta_4/6)
        print(y)
    return y

r1 = runga_kutta(0,1.4,0,0,0.1)
r2 = runga_kutta(0,1.4,0,0,0.1/2)
r3 = runga_kutta(0,1.4,0,0,0.1/4)
r4 = runga_kutta(0,1.4,0,0,0.1/8)
print("s1 =", r1) 

#era suposto dar
#s1 = 1.13312765
#s2 = 1.13311376
#s3 = 1.13311275 
quociente = (r2-r1)/(r3-r2)
print("quociente =", quociente)
quociente = (r3-r2)/(r4-r3)
print("quociente2 =", quociente)

        


