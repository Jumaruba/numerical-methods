#QUESTAO 3
import math as m 

def f1(x,y):
    return m.sin(x+y)-m.exp(x-y)
def df1x(x,y): 
    return m.cos(y+x)-m.exp(x-y)
def df1y(x,y):
    return m.cos(y+x)+m.exp(x-y)
def f2(x,y): 
    return m.cos(x+y)-x*x*y*y
def df2x(x,y): 
    return -m.sin(x+y)-2*x*y*y
def df2y(x,y): 
    return -m.sin(y+x)-2*x*x*y

def newton(x,y):
    for i in range(20): 
        jacobian = df1x(x,y)*df2y(x,y)-df2x(x,y)*df1y(x,y)
        xn = x - (f1(x,y)*df2y(x,y)-f2(x,y)*df1y(x,y))/jacobian 
        yn = y - (df1x(x,y)*f2(x,y)-df2x(x,y)*f1(x,y))/jacobian 
        x = xn
        y = yn 
        print(x, y)
        
        
newton(-1,0.5)
