import math as m 

def f(x,y): 
    return m.sin(y) + y*y/4 + m.cos(x) + x*x/4 -1 
def dfx(x,y): 
    return x/2 - m.sin(x)*y
def dfy(x,y): 
    return m.cos(y) + y/2 
def dfxx(x,y): 
    return 1/2 - m.cos(x)
def dfyy(x,y):
    return 1/2 - m.sin(y)
def dfxy(x,y): 
    return 0
def dfyx(x,y): 
    return 0

def quadrica(x,y):
    # se usar while loop da treta. Não sai do primeiro ciclo 
    for i in range(20): 
        x_ant = x
        y_ant = y 
        det = dfxx(x_ant,y_ant) * dfyy(x_ant,y_ant) - dfxy(x_ant,y_ant) * dfyx(x_ant,y_ant) 
        x = x_ant - (dfyy(x_ant,y_ant)*dfx(x_ant, y_ant) - dfxy(x_ant,y_ant)*dfy(x_ant,y_ant))/det
        y = y_ant - (-dfxy(x_ant, y_ant)* dfx(x_ant, y_ant) + dfxx(x_ant, y_ant) * dfy(x_ant, y_ant))/det
        print(x,y)
    return [x,y]

r = quadrica(0,0)
print(f(r[0],r[1]))