def x_(x,y,z): 
    return (7-y-z)/3

def y_(x,y,z):
    return (4-x-2*z)/4

def z_(x,y,z):
    return (5-2*y)/5


def jacobi(x,y,z):
    for i in range(30): 
        x_ant = x
        y_ant = y
        z_ant = z
        x = x_(x_ant, y_ant, z_ant);
        y = y_(x_ant, y_ant, z_ant);
        z = z_(x_ant, y_ant, z_ant); 
    print("%.10f, %.10f, %.10f" %(x,y,z))
    
jacobi(0,0,0)


def gauss(x,y,z):
    for i in range(30):
        x = x_(x, y, z);
        y = y_(x, y, z);
        z = z_(x, y, z); 
    print("%.10f, %.10f, %.10f" %(x,y,z))
    
gauss(0,0,0)