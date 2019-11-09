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
    x1_ant = x1
    x2_ant = x2
    x3_ant = x3
    for i in range(20):    
        x1 = _x1(x2,x3)
        x2 = _x2(x1,x3)
        x3 = _x3(x1,x2)
        print("x1: %f\t x2: %f\t x3: %f\t" %(x1,x2,x3))
        if (abs(x1-x1_ant) < 10**(-3) and abs(x2-x2_ant) < 10**(-3) and abs(x2-x2_ant) < 10**(-3)):     #checar o criterio de paragem
            break
        x1_ant = x1     
        x2_ant = x2 
        x3_ant = x3

gauss_Seidel(0,0,0)

    