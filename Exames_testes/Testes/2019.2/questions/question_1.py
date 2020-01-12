balanca = [
0.0000000000,
0.0620557145,
1.0558914326,
5.3775128776,
17.0202629218,
41.5748215863,
86.2292060414,
159.7687706061,
272.5762067482,
436.6315430847,
665.5121453814,
974.3927165529,
1380.0452966628,
1900.8392629238,
2556.7413296971,
3369.3155484932,
4361.7233079714]


def trapezio(h): 
    n = round(16/h)
    total = 0
    for i in range(1,n):
        total += 2*balanca[i*h]
    total += balanca[0] + balanca[16]
    total *= h/2 
    return total

def simpson(h): 
    n = round(16/h)
    total = 0
    for i in range(1,n,2):
        total += 4*balanca[i*h]
    for i in range(2,n,2):
        total+= 2*balanca[i*h]
    total+= balanca[0] + balanca[16]
    total*=h/3
    return total 

r1 = simpson(4)
r2 = simpson(2)
r3 = simpson(1)
print(r1,r2,r3)

quociente = (r2-r1)/(r3-r2)
print(quociente)
