def f1(x,y): 
    return x**2 - y -1.2 

def f2(x,y): 
    return -x + y**2 -1  

def df1x(x,y): 
    return 2*x

def df1y(x,y): 
    return -1 

def df2x(x,y):
    return -1 

def df2y(x,y):
    return 2*y 

def newton(x,y): 
    for _ in range(3):
        print(x,y) 
        x_ant = x 
        y_ant = y
        x = x_ant - (f1(x_ant,y_ant)*df2y(x_ant,y_ant) - f2(x_ant, y_ant)*df1y(x_ant,y_ant))/(df1x(x_ant,y_ant)*df2y(x_ant,y_ant)-df2x(x_ant, y_ant)*df1y(x_ant,y_ant))
        y = y_ant - (f2(x_ant,y_ant)*df1x(x_ant, y_ant) - f1(x_ant, y_ant)*df2x(x_ant,y_ant))/ (df1x(x_ant, y_ant) * df2y(x_ant,y_ant) - df2x(x_ant, y_ant)*df1y(x_ant,y_ant) )
    
newton(1,1)