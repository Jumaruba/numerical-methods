import math as m 

# parece com um sistema de equaçãoes diferenciais. 
# precisamos transformar a equação de ordem superior numa de 1 ordem
# o processo está explicado num arquivo pdf

def f(x,y,z):
    return z
def g(x,y,z):
    return x-3*z-2*y

def sistema(a,b,xn_1,yn_1,zn_1,h):
    while (xn_1 < b):
        xn = xn_1
        yn = yn_1
        zn = zn_1 
        xn_1 = xn + h
        delta_y1 = h * f(xn,yn,zn)
        delta_z1 = h * g(xn,yn,zn)

        delta_y2 = h * f(xn + h/2, yn+delta_y1/2, zn + delta_z1/2)
        delta_z2 = h * g(xn + h/2, yn+delta_y1/2, zn + delta_z1/2)

        delta_y3 = h * f(xn + h/2, yn+delta_y2/2, zn + delta_z2/2)
        delta_z3 = h * g(xn + h/2, yn+delta_y2/2, zn + delta_z2/2)

        delta_y4 = h * f(xn + h, yn+delta_y3, zn + delta_z3)
        delta_z4 = h * g(xn + h, yn+delta_y3, zn + delta_z3)

        yn_1 = yn +1/6*delta_y1 + 1/3*delta_y2 + 1/3*delta_y3 + 1/6*delta_y4
        zn_1 = zn +1/6*delta_z1 + 1/3*delta_z2 + 1/3*delta_z3 + 1/6*delta_z4
    print("%.10f" %xn_1)    
    return [yn_1, zn_1]


sistema(0,0.5,0,0,0,0.05)
#para y
r1 = sistema(0,0.5,0,0,0,0.05/2)[0]
r2 = sistema(0,0.5,0,0,0,0.05/4)[0]
r3 = sistema(0,0.499,0,0,0,0.05/8)[0]
print("y1: ", r1)
print("y2: ", r2)
print("y3: ", r3) 
quociente = (r2-r1)/(r3-r2)
print("quociente_y:", quociente)

z1 = sistema(0,0.5,0,0,0,0.05/2)[1]
z2 = sistema(0,0.5,0,0,0,0.05/4)[1]
z3 = sistema(0,0.499,0,0,0,0.05/8)[1]
print("z1: ", z1)
print("z2: ", z2)
print("z3: ", z3) 
quociente_z = (z2-z1)/(z3-z2)
print("quociente_z:", quociente_z)