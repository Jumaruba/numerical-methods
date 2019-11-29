import math as m

def f(x):
    return m.sin(x)

def tercos(a,b,prec):
    while (abs(b-a) > prec):
        prop = (b-a)/3
        c = a+prop
        d = b-prop
        if (f(c) > f(d)):
            a = c
        else: 
            b = d
    if(a == c): 
        return [c,d,b]
    else:
        return [a,c,d]


lista = tercos(3,6,0.0001)
print(lista) 