import math as m

def f(x):
	return x - 2*m.log(x)-5;

def falsiPosition(a,b): 
	def corda(a,b, error): 
	    x = 0
	    for i in range(20): 
		xn = (f(b)*a-f(a)*b)/(f(b)-f(a))
		if f(a)*f(xn)< 0:
		    b = xn 
		else:
		    a = xn 
		if abs((x-xn)) <= error:
		    print('f(a): {0:.10f}\t f(b): {1:.10f}\t x: {2:.10f}\t ' .format(f(a),f(b),x))
		    break
		
		print('f(a): {0:.10f}\t f(b): {1:.10f}\t x: {2:.10f}\t' .format(f(a),f(b),x))

		


falsiPosition(0.01,1)
