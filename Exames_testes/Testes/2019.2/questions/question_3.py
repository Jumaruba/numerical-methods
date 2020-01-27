#question 3 

def _x1(x1,x2,x3,x4): 
    return (-0.5*x2-3*x3-0.25*x4+2.5)/6
def _x2(x1,x2,x3,x4):
    return (-1.2*x1-0.25*x3-0.2*x4+3.8)/3
def _x3(x1,x2,x3,x4):
    return (x1-0.25*x2-2*x4+10)/4
def _x4(x1,x2,x3,x4):
    return (-2*x1-4*x2-x3+7)/8

def gauss_seidel(x1,x2,x3,x4):
    for i in range(1):
        x1 = _x1(x1,x2,x3,x4)
        x2 = _x2(x1,x2,x3,x4)
        x3 = _x3(x1,x2,x3,x4)
        x4 = _x4(x1,x2,x3,x4)
        
        print(x1,x2,x3,x4)
gauss_seidel(0,0,0,0)
    