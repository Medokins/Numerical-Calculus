import numpy as np
import matplotlib.pyplot as plt

N = 50
L = 10
delta_x = 2 * L / N
off_diagonal = -1 * (1 / (2 * pow(delta_x, 2)))

def generate_matrix(N):
    mtx = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if (i == j): mtx[i][j] = pow(delta_x, -2) + pow((-L + i * delta_x), 2) / 2
            elif (i + 1 == j or j + 1 == i): mtx[i][j] = off_diagonal
    return mtx

def QR(A):
    R = A
    N = A.shape[0]
    Q = np.eye(N)
    for i in range(N -1):
        temp = R[i:, i]
        e = np.zeros_like(temp)
        e[0] = np.linalg.norm(temp)
        U = temp - e

        V = U / np.linalg.norm(U)

        I = np.eye(N)
        Q_i = np.eye(N)

        Q_i[i:, i:] = I[i:, i:] - 2*np.outer(V, V)
        R = np.dot(Q_i, R)
        Q = np.dot(Q, Q_i)

    return Q, R

H = generate_matrix(N)
Q_cpy = generate_matrix(N)
Q, R = QR(H) 
P = np.eye(N)

for i in range(N):
    q, r = QR(Q_cpy)
    P = np.dot(P, q)
    Q_cpy = np.dot(r, q)

lambda_values = np.diag(Q_cpy)[::-1]
print("wartosci wlasne:", lambda_values[:L])

for i in range(1, 6):
    plt.plot(P[:, -i], markersize=5)
plt.grid()
plt.show()