import math as m
def f(x):
	return x - 2*m.log(x)-5;

def bissection(a,b):
	for i in range(20):
		mid = (a+b)/2
		if f(a)*f(mid) < 0: 
			b = mid
		else:
			a = mid

		print('f(a): {0:.10f}\t f(b): {1:.10f}\t mid: {2:.10f}\t ' .format(f(a),f(b),mid))


bissection(0.01,1)