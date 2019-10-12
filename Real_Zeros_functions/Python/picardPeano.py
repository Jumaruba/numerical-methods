import math as m

def g(x): 
	return 1/x+2.5	#apenas a raiz positiva

def f(x): 
	return 2*x*x-5*x-2

def picardPeano(x, max_iter):
	for i in range(max_iter):
		x = g(x)
		print(x)


picardPeano(3,20)
