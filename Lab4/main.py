import numpy as np
import pandas as pd

L = 10
N = 50
A = np.zeros((N, N))
delta_x = 2*L / N
off_diagonal = -1/(2*pow(delta_x, 2))

x = [-L + i*delta_x for i in range(1, N+1)]
for i in range(N):
    for j in range(N):
        if j == i:
            A[i][j] = pow(delta_x, -2) + pow((-L + i*delta_x), 2)/2
        elif j + 1 == i or j - 1 == i:
            A[i][j] = off_diagonal

def get_range(mtx):
  return [-(mtx[0][0] + abs(mtx[0][1])), mtx[0][0] + abs(mtx[0][1])]

def bisekcja(mtx, _a1, _a2, i, n):
    x = (_a1 + _a2)/2
    w = np.zeros(N)
    if(n == 0):
        return x
    generate(w, mtx, x)
    if(count(w) > i):
        _a2 = x
    else:
        _a1 = x
    x = (_a1 + _a2)/2
    return bisekcja(mtx, _a1, _a2, i, n - 1)

def count(w):
  count = 0
  for i in range(N-1):
      if((w[i] * w[i+1]) < 0):
          count += 1
  return count

def generate(w, mtx, x):
    w[0] = 1
    w[1] = mtx[0][0] - x
    for i in range(2, N):
      w[i] = (mtx[i-1][i-1] - x)*w[i-1] - pow(mtx[i][i-1],2)*w[i-2]


def calculate(vec, x, mtx):
    vec[0] = 1
    vec[1] = (x-mtx[0][0])/mtx[0][1]
    for i in range(2, N-1):
        vec[i] = ((x-mtx[i][i])*vec[i-1]-mtx[i-1][i]*vec[i-2])/mtx[i][i+1]

b = get_range(A)
w_n = 1
w_p = 0
values = np.zeros(5)

for i in range(5):
  values[i] = bisekcja(A, b[0], b[1], i, N)

print(values)
vect = np.zeros(N)
Result = {"iteartion": [], "value": []}
for i in range(5):
  calculate(vect, values[i], A)
  for j in range(50):
    Result["iteartion"].append(i+1)
    Result["value"].append(vect[j])

df = pd.DataFrame(Result)
df = df.set_index('iteartion')
df.to_csv("RESULTS.csv")