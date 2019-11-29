def x_(y,z): 
    return 6-y-z

def y_(x, z):
    return 3*x+z+2

def z_(x,y): 
    return 2-2*x

def gauss_jacobi(x,y,z): 
    for i in range(20): 
        x_ant = x 
        y_ant = y
        z_ant = z
        x = x_(y_ant, z_ant)
        y = y_(x_ant, z_ant)
        z = z_(x_ant, y_ant)

    return [x,y,z]


g = gauss_jacobi(10,10,10)
print("x: %f, y: %f, z: %f " %(g[0],g[1],g[2]))
