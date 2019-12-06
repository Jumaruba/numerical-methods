matrix = [[95, 3, 1, 2, 101],
          [4, 100, 10, 5, 119],
          [3, 9, 55, 5, 72],
          [10, 2, 4, 80, 96]]


def rowOp(down, up, k):
    global matrix
    for p in range(len(matrix[0])):
        matrix[down][p] -= k * matrix[up][p]


def gauss():
    global matrix
    for i in range(len(matrix)):
        rowOp(i, i, (1 - 1 / matrix[i][i]))
        for j in range(i, len(matrix)):
            if i != j:
                rowOp(j, i, matrix[j][i])


gauss()
for i in matrix:
    print(i)
