#question 4

h = 0.08
print(h/2)
print(h/4)
    

def dv(u,v):
    return u*(u/2+1)*v**3 + (u+5/2)*v**2 

def rk4(u,v,b,h):
    while(u < b-0.001):
        delta_1 = h*dv(u,v)
        delta_2 = h*dv(u+h/2, v + delta_1/2)
        delta_3 = h*dv(u+h/2, v + delta_2/2)
        delta_4 = h*dv(u+h,v+delta_3)
        delta = delta_1/6+delta_2/3+delta_3/3+delta_4/6
        v += delta
        u += h
    return v
    
    
    
r1 = rk4(1,0.15,1.8,0.08)
r2 = rk4(1,0.15,1.8,0.08/2)
r3 = rk4(1,0.15,1.8,0.08/4)
print(r1 )
print(r2 )
print(r3 )

qc = (r2-r1)/(r3-r2)
print(qc )
error = (r3-r2)/15
print(error)