matrix = [[2,-6,-1,-38],[-3,-1,7,-34],[-8,1,-2,-20]]

def rowOp(down, up ,k): 
    for i in range(len(matrix[0])): 
        matrix[down][i] -= k*matrix[up][i]

def Gauss():
    for i in range(len(matrix)):
        rowOp(i,i,1-1/matrix[i][i])
        for j in range(i,len(matrix)):
            if i!=j:
                rowOp(j,i,matrix[j][i])

Gauss()
for i in matrix:
    print(i)

#respostas encontrada: 
# z:    -2.000000000000014
# y:    8
# x:    4


# passos para achar estabilidade externa (maxima): 
# matrix_error: matrix([0.3,0.3,0.3],[0.3,0.3,0.3],[0.3,0.3,0.3])$
# matrix_b: matrix([0.3,0.3,0.3])$
# matrix_x: matrix([x],[y],[z])$
# matrix_k: matrix_b - matrix_error.matrix_x;
# matrix_orig: matrix([2,-6,-1],[-3,-1,7],[-8,1,-2]);
# invert(matrix_orig).matrix_k;
#                                          [  0.5151474530831093  ]
#                                          [                      ]
#(%o12)                                    [  0.7178284182305621  ]
#                                          [                      ]
#                                          [ - 0.1266756032171579 ]
# Estabilidade interna
#   matrix_orig.matrix_x;
#                                          [-38 + 37.99999999999998 ]
#                                          [                     ]
#(%o21)                                    [-34 + 34.0000000000001  ]
#                                          [                     ]
#                                          [-20 + 19.99999999999997 ]