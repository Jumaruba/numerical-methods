#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math as m 

#---------------------------------------------------------------
#QUESTAO 3
def f1(x,y): 
    return x+y-3
def df1x(x,y):
    return 1
def df1y(x,y): 
    return 1
def f2(x,y):
    return x*x+y*y-9
def df2x(x,y):
    return 2*x
def df2y(x,y):
    return 2*y

def newton(x,y,error): 
    for i in range(40): 
        jacobian = df1x(x,y)*df2y(x,y)-df1y(x,y)*df2x(x,y)
        xn = x - (f1(x,y)*df2y(x,y)-df1y(x,y)*f2(x,y))/jacobian
        yn = y - (df1x(x,y)*f2(x,y)-f1(x,y)*df2x(x,y))/jacobian
        if (abs((x - xn)/xn) <= error and abs((y-yn)/yn)<= error):
            print("%.10f\t %.10f\t" %(xn,yn))
            break
        print("%.10f\t %.10f\t" %(xn,yn))
        x = xn
        y = yn
#newton(4,1,0.05)
        
#---------------------------------------------------------------
#QUESTAO 2
def g(x): 
    return  m.exp(-x)   
def picardpeano(x, error): 
    for i in range(30): 
        xn = g(x)
        if (abs((xn-x)/xn)<= error):
            print("%.10f\t" %xn)
            break 
        x = xn
        print("%.10f\t" %xn)
    
picardpeano(1.1,0.05 )
#newton(4,1,0.05)
