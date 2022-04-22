import numpy as np
import matplotlib.pyplot as plt

N = 5
f = np.zeros((N+1,N+1))
x_min = -5
x_max = 5

def printArray(arrayToPrint, N):
    for i in range(N+1):
        for j in range(N+1):
            print(round(arrayToPrint[i][j], 5), end="   ")
        print("\n")

def set_x(n, min, max):
    step = (max-min)/(n)
    x = [min+(step*i) for i in range(n+1)]
    return x

def set_y(vector_x):
    y = [(1/(1+(x*x))) for x in vector_x]
    return y

def fillFirstColumn(f, N, vecotor_y):
    for i in range(N+1):
        f[i][0] = vecotor_y[i]
    return f

def createRightArray(f, n, x):
    for j in range(1, n+1):
        for i in range(j, n+1):
            f[i][j] = (f[i][j-1]-f[i-1][j-1]) / (x[i]-x[i-j])
    return f

def newton(x, f, vector_x): 
    result = 0.0
    for i in range(N+1):
        temp = f[i][i]
        for j in range(i):
            temp *= (x - vector_x[j])
        result += temp
    return result

x = set_x(N, x_min, x_max)
y = set_y(x)
f = fillFirstColumn(f, N, y)
rightArray = createRightArray(f, N, x)

x_points = []
y_points = []

for x in np.arange(-5, 5, 0.1):
    x_points.append(x)
    y_points.append(newton(x, rightArray, set_x(N, x_min, x_max)))

plt.plot(x_points, y_points, color="red")
plt.show()