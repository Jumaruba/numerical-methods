import math as m


def f1(x,y):
	return 2*x*x-x*y-5*x+1
def f2(x,y):
	return x+3*m.log10(x)-y*y
def gx(x,y):						#achando a funcao de x, com f1
	return (-2*x*x+5*x-1)/(-y)
def gy(x,y):						#achando a funcao y, com f2
	return (x+3*m.log10(x))/y

def picardPeano_2(x,y, max_iter): 
	for i in range(max_iter):
		x = gx(x,y)
		y = gy(x,y)
		print('x: %1.7f\t y:%1.7f\t '%(x,y))

picardPeano_2(10,0,20)