
import numpy as np
import random
import matplotlib.pyplot as plt

def homogeneou(x_0, a, c, m, n):
  arr = [x_0/(m+1)]
  for i in range(n):
    x = (a*x_0 + c) % m
    arr.append(x/(m+1))
    x_0 = x
  return arr

def triangular(mi, n):
  return [mi + (random.uniform(0,1) + random.uniform(0,1) - 1) * delta for _ in range(n)]

def F(x, u):
  if x<=u:
    return((-1/pow(delta,2)) * (-(pow(x,2)/2) + u*x) + (x/delta) - ((-1/pow(delta,2)) * (-pow((u-delta),2)/2 + u*(u-delta)) + (u-delta)/delta))
  else:
    return((-1/pow(delta,2)) * (pow(x,2)/2 - u*x) + x/delta - (-1/pow(delta,2) * (pow(u,2)/2 - pow(u,2)) + u/delta) + 1/2)

def check(arr, n):
    mi = 1/n*sum([i for i in arr])
    sigm = (1/n*sum([pow(i-mi, 2) for i in arr]))**0.5
    print(mi, sigm)

x_0 = 10
n1 = 10**4
k = 12

a = 123
c = 1
m = 2**15

a2 = 69069
c2 = 1
m2 = 2**32

arr1 = homogeneou(x_0, a, c, m, n1)
arr2 = homogeneou(x_0, a2, c2, m2, n1)

check(arr1, n1)
check(arr2, n1)

##################################

mi = 4
delta = 3
n = 10**3
K = 10

triangle_arr = triangular(mi, n)

a = mi - delta
b = mi + delta
h = (b - a) / K

bins = np.zeros(K)
for number in triangle_arr:
  for j in range(K):
    if number < a + (j+1) * h:
      bins[j] += 1
      break

arr_val = [F(i+h, mi) - F(i, mi) for i in np.arange(a, b, h)]

test = sum([pow(bins[i] - n*arr_val[i],2) / (n*arr_val[i]) for i in range(K)])

plt.plot(arr2[0:n1-1:], arr2[1:n1:], linestyle = ' ', marker = '.')
plt.xlabel('$X_{i}$')
plt.ylabel('$X_{i+1}$')
plt.show()

plt.hist(arr1, density = True, color = 'b', edgecolor = 'r', bins = k)
plt.hist(arr2, density = True, color = 'b', edgecolor = 'r', bins = k)
plt.xlabel('$X$')
plt.ylabel('$P(X)$')
plt.show()

plt.hist(triangle_arr, density = True, color = 'b', edgecolor = 'r', bins = K)

plt.bar([i for i in np.arange(a, b, h)], bins/n, color = 'b', edgecolor = 'r', width=0.5)
plt.plot([i for i in np.arange(a, b, h)], arr_val, 'r', label='$p_i$', marker = 'o')
plt.xlabel('$X$')
plt.ylabel('$n_i/N$')
plt.show()