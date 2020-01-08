import math as m 

def f1(x): 
    return m.exp(x)-x-77
def df1(x): 
    return m.exp(x)-1 
def g1(x): 
    return m.exp(x)-77
def g2(x): #CONVERGE
    return m.log(x+77)
def g3(x): 
    return x - f1(x)/df1(x)

def picardPeano1(x): 
    for i in range(30): 
        x = g1(x)
        print(i, x) 

def picardPeano2(x): 
    for i in range(30): 
        x = g2(x)
        print(i, x) 

def picardPeano3(x): 
    for i in range(30): 
        x = g3(x)
        print(i, x) 
    
picardPeano1(4)
picardPeano2(4)
picardPeano3(4)
