#formulas de recorrência
def _x1(x2,x3): 
    return (7-x2-x3)/3

def _x2(x1,x3):
    return (4-x1-2*x3)/4

def _x3(x1,x2):
    return (5-2*x2)/5

matrix = [[3,1,1,7],
          [1,4,2,4],
          [0,2,5,5]]

def gauss_Seidel(x1,x2,x3):     


    