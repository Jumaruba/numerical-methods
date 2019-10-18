import math as m

#estas funcoes devolvem um erro de divisao por zero, mas tentando com outra funcao, da certo
def f1(x,y):
	return 2*x*x-x*y-5*x+1
def f2(x,y):
	return x+3*m.log10(x)-y*y
def gx(x,y):						#achando a funcao de x, com f1
	return m.pow((x*y+5*x-1)/2, 1/2)
def gy(x,y):						#achando a funcao y, com f2
	return m.pow(x+3*m.log(x),1/2)

#gauss seil
def picardPeano_2_error(x,y, erro):
	x = 1
	y = 1
	xAnt = 2
	yAnt = 2
	while(abs(xAnt-x)>=erro or abs(yAnt-y)>=erro):
		xAnt = x
		yAnt = y
		x = gx(x,y) 
		y = gy(xAnt,y) 
		print('x: %1.7f\t y:%1.7f\t' %(x,y))
	

def picardPeano_2(x,y, max_iter): 

	for i in range(max_iter):
		xAnt = x
		x = gx(x,y)
		y = gy(xAnt,y)
		print('x: %1.7f\t y:%1.7f\t '%(x,y))

picardPeano_2(10,0,20)
print("")
picardPeano_2_error(10,0,m.pow(10,-5))