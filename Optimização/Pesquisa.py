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
