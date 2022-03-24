import numpy as np
import pandas as pd  # to potrzebne tylko do zapisu wyniku do pliku csv
import matplotlib.pyplot as plt  # to potrzebne tylko do wykresow

n = 1000
m = 5
iterator = 0
mode = "a"

Result = {"iteartion": [], "Norm R": [], "alpha": [], "Norm X": []}
plotPoints_x = []
plotPointsX_y = []
plotPointsR_y = []

A = np.empty([n, n])
B = np.empty(n)
R = np.empty(n)

if mode == "a":
    X = np.zeros(n)
if mode == "b":
    X = np.ones(n)

for i in range(n):
    B[i] = i
    for j in range(n):
        value = abs(i - j)
        if(value <= m and i, j < n):
            A[i][j] = 1 / (1 + value)
        else:
            A[i][j] = 0

R = np.subtract(B, np.dot(A, X))

while(np.linalg.norm(R) > pow(10, -6)):

    R = np.subtract(B, np.dot(A, X))
    alpha = np.dot(np.transpose(R), R) / np.dot(np.dot(np.transpose(R), A), R)
    X = np.add(X, np.dot(alpha, R))

    Result["iteartion"].append(iterator)
    Result["Norm R"].append(np.linalg.norm(R))
    Result["alpha"].append(alpha)
    Result["Norm X"].append(np.linalg.norm(X))

    plotPoints_x.append(iterator)
    plotPointsX_y.append(np.linalg.norm(X))
    plotPointsR_y.append(np.linalg.norm(R))

    iterator += 1

df = pd.DataFrame(Result)
df = df.set_index('iteartion')
df.to_csv("RESULTS.csv")



plt.plot(plotPoints_x, plotPointsX_y, color = (1,0,0))
plt.plot(plotPoints_x, plotPointsR_y, color = (0,1,0))
plt.yscale('log')

plt.ylabel("Norm X (red) R (green)")
plt.xlabel("Iteration")
plt.show()