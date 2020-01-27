
def z(x,y):
    return 3*x**2 - x*y + 11*y + y**2 - 8*x 

def dfx(x,y): 
    return -y + 6*x - 8


def dfy(x,y):
    return 2*y - x +11

def gradient(x,y, lamb):
    for i in range(60):
        print(i, x,y)
        x_ = x - lamb*dfx(x,y)
        y_ = y - lamb*dfy(x,y)
        if (abs(x_-x) <= 0.001 and abs(y_-y)<=0.001):
            break
        print(i, abs(x_-x), abs(y_-y)) 
        if (z(x_,y_) < z(x,y)):
            lamb *=2
            x = x_
            y = y_
        else: 
            lamb/=2

print("----GRADIENT 1 ----")
gradient(2,2,1)
#10 -0.15625 -5.34375
#10 0.8984375 0.1171875
#29 0.0053551048040390015 0.0006984919309616089
#29 0.4527251422405243 -5.272938936948776
#demora 34 passos para terminar
print("----GRADIENT 0.5 ----")
#Tem quase os mesmos passos do gradiente, mas no começo tem resultados mais precisos
gradient(2,2,0.5)
#9 0.4296875 -5.109375
#9 0.078125 0.087890625
#24 0.4543083906173706 -5.271169424057007
#24 0.0014901161193847656 0.0016763806343078613
print("----GRADIENT 0.25 ----")
gradient(2,2,0.25)
#No começo tem resultados menos precisos do que gradiente 0.5
#9 0.5078125 -5.197265625
#9 0.1220703125 0.048828125
#23 0.4543083906173706 -5.271169424057007
#23 0.0014901161193847656 0.0016763806343078613

#Conclusão:
#O melhor lamda é o maior lambda < 1 com o menor número de iterações possíveis. 