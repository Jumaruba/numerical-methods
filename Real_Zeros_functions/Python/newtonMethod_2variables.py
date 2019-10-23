import math as m


def f1(x,y):
	return 2*x*x-x*y-5*x+1

def f2(x,y): 
	return x+3*m.log10(x)-y*y

def df1x(x,y):
	return -y+4*x-5

def df2x(x,y): 
	return 3/(m.log(10)*x)+1

def df1y(x,y):
	return -x

def df2y(x,y):
	return -2*y
	
def newtonMethod_2(x, y): 
	for i in range(20): 
		jacobian = df1x(x,y)*df2y(x,y)-df1y(x,y)*df2x(x,y)
		xn = x - (f1(x,y)*df2y(x,y)-df1y(x,y)*f2(x,y))/jacobian
		yn = y - (df1x(x,y)*f2(x,y) - f2(x,y)*df1x(x,y))/jacobian
		y = yn
		x = xn
		print('n: {2}\t x: {0:.10f}\t y: {1:.10f}'.format(x,y,i))

newtonMethod_2(1,2)
