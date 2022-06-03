import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

m = 0
k = 1
n = 30
# range of Integral
a = 0
b = np.pi

summ_df = {'l': [], 'summ': []}
simpson_df = {'l': [], 'simpson': []}

def fun(x,m,k):
  return np.power(x,m) * np.sin(k*x)

def series(x, m, k, n):
    summ = 0
    for i in range(n):
        summ += (np.power(-1, i)*np.power(k*x, 2*i+m+2))/(np.power(k, m+1)*np.math.factorial(2*i+1)*(2*i+m+2))
    return summ

def I(a, b, m, k, n):
  return series(b,m,k,n) - series(a, m, k, n)

def simpson(a, b, m, k, n):
    p = (n-1)//2
    h = (b-a)/(2*p)
    summ = 0
    r = a + 2*h
    l = a
    for _ in range(p):
        c = (r + l) / 2
        summ += (1/3)*h*(1*fun(l, m, k) + 4*fun(c, m, k) + 1*fun(r, m, k))
        l = r
        r += 2*h
    return summ

#########################################################
print(f"For m = {m}, k = {k}\nWith I: {I(a, b, m, k, n)}")
print(f"With simpson: {simpson(a, b, m, k, n)}")

for l in range(n):
    summ_df['l'].append(n)
    summ_df['summ'].append(I(a, b, m, k, l))

n_arr = [11, 21, 51, 101, 201]
for i in n_arr:
    simpson_df['l'].append(i)
    simpson_df['simpson'].append(simpson(a, b, m, k, i))

plt.plot([n for n in n_arr], [abs(C-summ_df['summ'][-1]) for C in simpson_df['simpson']], marker = '.')
plt.xlabel('$n$ - number of nodes')
plt.ylabel('$|C-I|$')
plt.yscale("log")
plt.show()

summ_df = pd.DataFrame.from_dict(summ_df)
simpson_df = pd.DataFrame.from_dict(simpson_df)

summ_df.to_csv(f"summ_df_{m}_{k}.csv")
simpson_df.to_csv(f"simpson_df_{m}_{k}.csv")