import math as m

def f(x): 
	return 2*x*x-5*x-2
def df(x): 
	return 4*x-5

def newtonMethod(x, max_iter):
	for i in range(max_iter):
		x = x - f(x)/df(x)
		print(x)



newtonMethod(3,20)

