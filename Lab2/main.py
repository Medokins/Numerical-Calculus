import numpy as np

X = [-2, -1, -0.5, 0.1, 0.3, 1.8]

C = [1, -0.5, 1, 1.5, -2, -0.5]

A = np.zeros([len(X), len(C)])

for i in range(len(X)):
    for j in range(len(C)):
        A[i][j] = pow(X[i], j)

size = len(A)
Y = np.dot(A, C)


def printMatrix(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end=5*" ")
        print("\n")


def luDecomposition(mat, n):  #Mat is matrix, N is size

    lower = np.identity(n)
    upper = mat

    # Upper
    for i in range(n):
        for j in range(i+1, size):
            l = upper[j][i]/upper[i][i]
            lower[j][i] = l
            for k in range(n):
                upper[j][k] = upper[j][k] - (l * upper[i][k])

    return lower, upper


L, U = luDecomposition(A, size)

z = np.dot(np.linalg.inv(L), Y)

C_unknown = np.dot(np.linalg.inv(U), z)
print(C_unknown)