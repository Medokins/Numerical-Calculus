import numpy as np
import matplotlib.pyplot as plt

# integral functions
def c1(x):
    return x/(4*pow(x,2)+1)

# For a = 2, c = 1
def c1a(x1, x2):
    return 1/8*(np.log(np.math.fabs(4*x2**2+1)) - np.log(np.math.fabs(4*x1**2+1)))

def c2(x, k):
    return np.power(x, k) #* np.exp(-x)

def c2a(k):
    return np.math.factorial(k)

def c3(x, y):
    return np.power(np.sin(x), 2) * np.power(np.sin(y), 4) #* np.exp(-np.power(x, 2) - np.power(y, 2))

c3a = 0.1919832644

# different methods
def Legandre(a, b, n):
    x, w  = np.polynomial.legendre.leggauss(n)
    x = (a + b)/2 + (b-a)*x/2
    suma = 0
    for i in range(n):
        suma += c1(x[i]) * w[i]
    return suma

def Laguerre(k, n):
    x,w  = np.polynomial.laguerre.laggauss(n)
    suma = 0
    for i in range(n):
        suma += c2(x[i], k) * w[i]
    return suma

def Hermite(n):
    x, w = np.polynomial.hermite.hermgauss(n)
    suma = 0
    for i in range(n):
        for j in range(n):
            suma += c3(x[i], x[j]) * w[i] * w[j]
    return suma

#######################################################

k = 10

arrLegandre = []
for n in range(2, 21):
    arrLegandre.append(Legandre(0, 2, n))

arrLaguerre = []
for n in range(2, 21):
    arrLaguerre.append(Laguerre(k, n))

arrHermite = []
for n in range(2, 16):
    arrHermite.append(Hermite(n))

print(np.average(arrLegandre))

print(f"Analitic c1: {c1a(0,2)}, Legandre: {np.average(arrLegandre)}", )
print(f"Analitic c2: {c2a(k)}, Laguerre: {arrLaguerre[-1]}", )
print(f"Analitic c3: {c3a}, Hermite: {(arrHermite[-1])}")

#########################################################

# 1 #####################################################
# Plot |c1 − c1,a| = f(n), n = 2, 3, . . . , 20
plt.plot(range(2, 21), [np.math.fabs(arrLegandre[i] - c1a(0,2)) for i in range(len(arrLegandre))])
plt.yscale("log")
plt.xlabel("n")
plt.ylabel("|$c_1-c_{1,a}|$")
plt.show()

# Summ of quadrature factors for every n
plt.plot(range(2, 21), arrLegandre)
plt.xlabel("n")
plt.ylabel("c1(n)")
plt.show()

# Plot of integral function.
plt.plot(np.arange(0, 2.1, 0.1), [c1(x) for x in np.arange(0, 2.1, 0.1)])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

# 2 ######################################################

# Plot |c2 − c2,a| = f(n) for k = 5
plt.plot(range(2, 21), [np.math.fabs(arrLaguerre[i] - c2a(5)) for i in range(len(arrLaguerre))])
plt.yscale("log")
plt.xlabel("n")
plt.ylabel("|$c_2-c_{2,a}|$")
plt.show()

# Plot |c2 − c2,a| = f(n) for k = 10
plt.plot(range(2, 21), [np.math.fabs(arrLaguerre[i] - c2a(10)) for i in range(len(arrLaguerre))])
plt.yscale("log")
plt.xlabel("n")
plt.ylabel("|$c_2-c_{2,a}|$")
plt.show()

# Summ of quadrature factors for every n
plt.plot(range(2, 21), arrLaguerre)
plt.xlabel("n")
plt.ylabel("c2(n)")
plt.show()

# Plot of integral function.
plt.plot(np.arange(0, 31, 1), [c2(x, 5) for x in np.arange(0, 31, 1)])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

# 3 #####################################################

# |c3 − cdok| = f(n)
plt.plot(range(2, 16), [np.math.fabs(arrHermite[i] - c3a) for i in range(len(arrHermite))])
plt.yscale("log")
plt.xlabel("n")
plt.ylabel("$|c_3-c_{3,a}|$")
plt.show()