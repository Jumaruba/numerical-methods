matrix = [[3,-1,2,-1],
          [1,1,1,8],
          [2,0,1,5]]

def rowOp(down, up, k): 
    for i in range(len(matrix[0])):
        matrix[down][i] -= k*matrix[up][i]
        
def gauss():
    for i in range(len(matrix)):
        rowOp(i,i,1-1/matrix[i][i])
        for j in range(i,len(matrix)):
            if i!= j:
                rowOp(j,i,matrix[j][i])
                
                
gauss()

for i in matrix:
    print(i)
    
    
    #4 7 -3 
# fazendo os passos no maxima: 
    
# z: -3.0000000000000018$
# y: 6.25 - 0.2500000000000001*z;
# (output) y = 7.000000000000001
#  x: -0.33333333333333326 + 0.33333333333333326*y - 0.6666666666666665*z;
# (output) x: 4.000000000000001

# X: matrix([x],[y],[z])$
# m: matrix([0.5,0.5,0.5],[0.5,0.5,0.5],[0.5,0.5,0.5])$
# b: matrix([0.5], [0.5],[0.5])$
# k: b -m.X$
# output                            [ - 3.5 ]
#                                   [       ]
#(%o8)                              [ - 3.5 ]
#                                   [       ]
#                                   [ - 3.5 ]
#orig:invert(matrix([3,-1,2],[1,1,1],[2,0,1])); 
#orig.k;
#                                  [ - 1.75 ]
#                                  [        ]
#(%o16)                            [ - 1.75 ]
#                                  [        ]
#                                  [  0.0   ]
    
#a estabilidade interna é 
# 0.000000000000001
# 0
# 0


#INTERPRETAÇAO
#Na estabilidade externa pdoemos dizer que x e y são igualmente afetados pelos erros e z não é afetado. 
#A estabilidade interna se refere ao quanto uma variável é afetada por arredondamentos e truncamentos. 
#Na nossa solução, apenas o x é afetado por estes, mas é muito pouco.