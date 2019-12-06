import math as m

def f(x):
    return (2*x+1)**2-5*m.cos(10*x)

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


def aurea_min(x1,x2, error):
    b = (m.sqrt(5)-1)/2
    a = b*b
    while(abs(x1-x2) > error):
        x3 = x1 + a*(x2-x1)  
        x4 = x1 + b*(x2-x1)
        if f(x3) < f(x4):
            x1 = x1 
            x2 = x4
        else:
            x1 = x3
            x2 = x2 
    return [x1,x2,x3,x4]

def aurea_max(x1,x2, error):
    b = (m.sqrt(5)-1)/2
    a = b*b
    while(abs(x1-x2) > error):
        x3 = x1 + a*(x2-x1)  
        x4 = x1 + b*(x2-x1)
        if f(x3) > f(x4):
            x1 = x1 
            x2 = x4
        else:
            x1 = x3
            x2 = x2 
    return [x1,x2,x3,x4]

print(aurea_min(-1,0,0.001))
print(aurea_max(-1,0,0.001))