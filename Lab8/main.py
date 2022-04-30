import numpy as np
import matplotlib.pyplot as plt
import math

x_min = -5
x_max = 5
n = 15

def set_M(vector_y, n, alfa, beta):

    h = (x_max-x_min)/(n-1)
    lamb = h/(h+h)
    mikro = 1 - lamb

    A = np.zeros((n,n))
    d = np.zeros(n)
    
    A[0][0] = 1.0
    A[n-1][n-1] = 1.0
    d[0] = alfa
    d[n-1] = beta

    for i in range(1, n-1):
        A[i][i] = 2.0 #diagonal
        A[i][i-1] = mikro #mikro
        A[i][i+1] = lamb #lambda
        d[i] = 6/(2*h) * ((vector_y[i+1]-vector_y[i])/h - (vector_y[i]-vector_y[i-1])/h) #vector

    print(d)
    w = np.linalg.solve(A,d)
    return w

def set_Sx(vector_x, vector_y, m, n, x):
    h = (x_max-x_min)/(n-1)
    for i in range(n):
        if x >= vector_x[i-1] and x <= vector_x[i]:
            A = (vector_y[i]-vector_y[i-1])/h - (h/6)*(m[i]-m[i-1])
            B = vector_y[i-1] - m[i-1] * h * h/6
            Sx = m[i-1] * math.pow((vector_x[i]-x), 3)/(6*h) + \
            m[i]*math.pow((x-vector_x[i-1]), 3)/(6*h) + A*(x-vector_x[i-1]) + B
    return Sx

def derivative(delta_x):
    d_f = [(y1(x-delta_x) - 2*y1(x) + y1(x+delta_x))/delta_x**2 for x in np.arange(-5, 5, delta_x)]
    return d_f

def set_y1(vector_x):
    y = [(1/(1+(x*x))) for x in vector_x]
    return y
 
def set_y2(vector_x):
    y = [(np.cos(2*x)) for x in vector_x]
    return y

def set_x(size, min, max):
    step = (max-min)/(size-1)
    x = [min+(step*i) for i in range(size)]
    return x

def y1(x):
    return 1/(1+(x*x))

###################################################################

alpha = 0
beta = 0
delta_x = 0.01

vector_x = set_x(n, x_min, x_max)
vector_y = set_y2(vector_x)

m = set_M(vector_y, n, alpha, beta)
s = [set_Sx(vector_x, vector_y, m, n, i) for i in vector_x]

derivative_from_formula = derivative(delta_x)

plt.plot(np.arange(-5,5,delta_x), [set_Sx(vector_x,vector_y,m,n,i) for i in np.arange(-5,5,delta_x)], linestyle='-')
plt.plot([i for i in vector_x], [i for i in s], linestyle='', marker="o")
plt.plot(np.arange(-5,5,delta_x), [1/(x*x+1) for x in np.arange(-5,5,delta_x)])
plt.show()