import numpy as np
import math
import pandas as pd

draw_figure = True
epsilon = 1e-3
h = 0.1
delta = 1e-4
r = [-0.75, 1.75]

data = {'x': [r[0]], 'y': [r[1]]}

def f(x, y):
    return (5 / 2) * math.pow((math.pow(x, 2) - y), 2) + math.pow((1 - x), 2)

def get_next_r(r):
    x = r[0] - h * ((f(r[0] + delta, r[1]) - f(r[0] - delta, r[1])) / (2 * delta))
    y = r[1] - h * ((f(r[0], r[1] + delta) - f(r[0], r[1] - delta)) / (2 * delta))
    return [x, y]

###############################################
previous = get_next_r(r)

for i in range(1000):
    next = get_next_r(previous)
    data['x'].append(next[0])
    data['y'].append(next[1])
    if(np.linalg.norm(np.subtract(next, previous)) < epsilon):
        print(next, i)
        break
    previous = next
    if i == 999:
        print(next, 1000)

df = pd.DataFrame(data)
if len(data['x']) < 50:
    df.to_csv("Results1e-2.csv")
else:
    df.to_csv("Results1e-3.csv")

if draw_figure:
    import matplotlib.pyplot as plt
    plt.plot(data['x'], data['y'])
    plt.show()