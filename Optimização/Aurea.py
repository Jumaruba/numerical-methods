import math as m

def f(x):
    return m.sin(x)

#estamos procurando pelo minimo local 
def pesquisa(guess, step): 
    if(f(guess) < f(guess+step)):
        step  -= step 

    x0 = guess 
    x1 = guess + step 
    x2 = guess + 2*step 
    while(f(x1) > f(x2)):
        x0 = x1 
        x1 = x2
        x2 = x2 + step
    print(x0,x1,x2)
    return [x0,x1,x2]

lista = pesquisa(2,0.1)

def tercos(a,b,prec):
    while (abs(b-a) > prec):
        prop = (b-a)/3
        c = a+prop
        d = b-prop
        if (f(c) > f(d)):
            a = c
        else: 
            b = c
    if(a == c): 
        return [c,d,b]
    else:
        return [a,c,d]

lista = tercos(3,6,0.0001)
print(lista) 