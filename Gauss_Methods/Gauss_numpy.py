import numpy as np
from scipy.linalg import lu

np.set_printoptions(formatter={'float': lambda x: "{0:0.10f}".format(x)})  # format the number of decimal cases

matrix = np.array([[95., 3., 1., 2., 101.],
                   [4., 100., 10., 5., 119.],
                   [3., 9., 55., 5., 72.],
                   [10., 2., 4., 80., 96.]])

p, l, u = lu(matrix)  # transforming it into a triangular matrix
for i in range(len(u)):  # diagonal to 1
    u[i] -= (1 - 1 / u[i][i]) * u[i]

print(u)
