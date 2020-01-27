import math as m 

def f(x): 
    return m.sin(x) + x**5 - 0.2*x +1 

def bissec():
    a = -1
    b= 0
    m = 0
    for i in range(8): 
        print("%i | %.7f | %.7f | %.7f " %(i, m, a,b))
        m = (a+b)/2 
        if (f(a)*f(m)< 0 ):
            b = m 
        else: 
            a = m 
        
    
bissec()

#valor final: 
#-0.5

# O valor absoluto seria: 
print("Valor absoluto: -0.83 + 0.82812=", (-0.82813  +0.84375))