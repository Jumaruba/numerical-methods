import math as m

matrix = [[1, 1 / 2, 1 / 3, -1], [1 / 2, 1 / 3, 1 / 4, 1], [1 / 3, 1 / 4, 1 / 5, 1]]


def rowOp(down, up, k):
    for i in range(len(matrix[0])):
        matrix[down][i] -= k * matrix[up][i]


def gauss():
    for i in range(len(matrix)):
        rowOp(i, i, (1 - 1 / matrix[i][i]))
        for j in range(i, len(matrix)):
            if i != j:
                rowOp(j, i, matrix[j][i])


gauss()
for i in matrix:
    print(i)

# calculando variáveis
z = matrix[2][3]
y = matrix[1][3] - matrix[1][2] * z
x = matrix[0][3] - matrix[0][2] * z - matrix[0][1] * y
print("X = %.5f || Y = %.5f || Z = %.5f" % (x, y, z))

# Para achar a estabilidade externa pelo máxima

#(%i1) a: matrix([0.05],[0.05],[0.05])$

# (%i2) b: matrix([0.05,0.05,0.05],[0.05,0.05,0.05],[0.05,0.05,0.05])$

# (%i3) orig: invert(matrix([1,1/2,1/3],[1/2,1/3,1/4],[1/3,1/4,1/5]))$

# (%i4) X: matrix([-15],[48],[-30])$

# (%i5) r: orig.(a-b.X);
#                           [ - 0.3000000000000012 ]
#                           [                      ]
# (%o5)                      [  2.400000000000009   ]
#                           [                      ]
#                           [ - 3.000000000000011  ]
#(%i6) orig: matrix([1,1/2,1/3],[1/2,1/3,1/4],[1/3,1/4,1/5])$