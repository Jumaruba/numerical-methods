def x1_(x1,x2,x3,x4): 
    return (1+x2+x3-x4)/4.5
def x2_(x1,x2,x3,x4):
    return (-1+x1-x3+x4)/4.5
def x3_(x1,x2,x3,x4):
    return (-1+x1-2*x2+x4)/4.5
def x4_(x1,x2,x3,x4): 
    return (-2*x1+x2+x3)/4.5

def gauss_jacobi(x1,x2,x3,x4):
    for i in range(20): 
        print("iteracao", i) 
        x1_a = x1 
        x2_a = x2 
        x3_a = x3
        x4_a = x4 
        x1 = x1_(x1_a,x2_a, x3_a,x4_a)
        x2 = x2_(x1_a,x2_a, x3_a,x4_a)
        x3 = x3_(x1_a,x2_a, x3_a,x4_a) 
        x4 = x4_(x1_a,x2_a, x3_a,x4_a) 
        print("x1: %.5f \t x2: %.5f" %(x1,x2))

gauss_jacobi(0.25,0.25,0.25,0.25)
