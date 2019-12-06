def x1_(x1,x2,x3):
    return (-38+x3+6*x2)*1/2
def x2_(x1,x2,x3): 
    return (34+7*x3-3*x1)
def x3_(x1,x2,x3):
    return (20-8*x1+x2)*1/2

def gauss_seidel(x1,x2,x3): 
    for i in range(20): 
        x1 = x1_(x1, x2,x3)
        x2 = x2_(x1, x2,x3)
        x3 = x3_(x1, x2, x3)
        print(x1,x2,x3)

def gauss_jacobi(x1,x2,x3): 
    for i in range(20): 
        x1_ant = x1
        x2_ant = x2
        x3_ant = x3
        x1 = x1_(x1_ant, x2_ant,x3_ant)
        x2 = x2_(x1_ant, x2_ant,x3_ant)
        x3 = x3_(x1_ant, x2_ant, x3_ant)
        print(x1,x2,x3)

gauss_seidel(3,3,3)
