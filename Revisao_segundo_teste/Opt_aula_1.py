import math as m
#levenberg marquadt 
def f(x,y):
    return m.sin(y) + y**2/4 + m.cos(x) + x**2/4 -1
def dfx(x,y):
    return x/2 - m.sin(x)
def dfy(x,y):
    return m.cos(y)+y/2
def dfxx(x,y):
    return 1/2 - m.cos(x)
def dfyy(x,y):
    return 1/2 - m.sin(y)
def dfxy(x,y):
    return 0
def dfyx(x,y):
    return 0

def levemberg(x,y, lamb):     
    for i in range(22):
        print("%i || X = %.5f || Y = %.5f" %(i, x, y))
        det = dfyy(x,y)*dfxx(x,y) + dfyx(x,y)*dfxy(x,y)
        xn = x - ((dfyy(x,y)*dfx(x,y) - dfyx(x,y)*dfy(x,y))/det + lamb*dfx(x,y))
        yn = y - ((-dfxy(x,y)*dfx(x,y) + dfxx(x,y)*dfy(x,y))/det + lamb*dfy(x,y))
        
        
        if f(xn,yn) < f(x,y):  #a nova operação foi bem sucedida
            lamb/=2
        else:           
            lamb*=2            

            
        x = xn 
        y = yn 
    return [x,y]

levemberg(1,1,0.1)