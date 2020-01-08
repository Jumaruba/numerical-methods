matrix = [[1,3,2,6],[1,-1,0,-2],[1,0,1,2]]


def rowOp(down,up,k):
    for p in range(len(matrix[0])):
        matrix[down][p] -= k*matrix[up][p]

def gauss():
    for i in range(len(matrix)):
        rowOp(i,i,1-1/matrix[i][i])
        for j in range(i,len(matrix)): 
            if i!=j:
                rowOp(j,i,matrix[j][i])

gauss()
for i in matrix:
    print(i)