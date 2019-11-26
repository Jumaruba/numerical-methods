def x_(x,y,z):
    return (-38+6*y+z)/2
def y_(x,y,z):
    return -(-34+3*x-7*z)
def z_(x,y,z): 
    return -(-20+8*x-y)/2

#antes de começar a fazer a questão note que esta não é uma matriz
#diagonalmente predominante, logo o metodo diverge!
def gauss_jacobi(x,y,z):
    for i in range(80): 
        x_anterior = x
        y_anterior = y
        z_anterior = z
        x = x_(x_anterior, y_anterior, z_anterior)
        y = y_(x_anterior, y_anterior, z_anterior)
        z = z_(x_anterior, y_anterior, z_anterior)
        print(x,y,z)


def gauss_seidel(x,y,z):
    for i in range(50): 
        x = x_(x,y,z)
        y = y_(x,y,z)
        z = z_(x,y,z)
        print(x,y,z)

gauss_seidel(2,2,2)