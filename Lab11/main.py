import numpy as np
import matplotlib.pyplot as plt

k = 8
N = 2 ** k
T = 1
t_max = 3*T
dt = t_max/N
sigma = T/20
omega = 2*np.pi/T

t = [i for i in np.arange(0, t_max, dt)]
f_0 = [np.sin(omega*i)+np.sin(2*omega*i)+np.sin(3*omega*i) for i in t]
f = [i + np.random.uniform(-0.5, 0.5) for i in f_0]

g1 = np.asarray([1/(sigma*np.sqrt(2*np.pi))*np.exp(-(i**2)/(2*sigma**2)) for i in t])
g2 = np.asarray([1/(sigma*np.sqrt(2*np.pi))*np.exp(-((-i)**2)/(2*sigma**2)) for i in t])

g = g1 + g2

f_f = np.fft.fft(f)
g_f = np.fft.fft(g)
fg = np.multiply(f_f, g_f)

fg2 = np.fft.ifft(fg)
f_max = np.amax([abs(i) for i in fg2])

plt.scatter([i for i in t], [i for i in f], 3, color='red')
plt.scatter([i for i in t], [i for i in f_0], 3, color='green')
plt.plot([i for i in t], [i*2.5/f_max for i in fg2], color='blue')
plt.legend(['splot', 'zaburzony', 'niezaburzony'])
plt.show()