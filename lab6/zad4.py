import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand
a = 1
l = 1
N = 2000
h_n = 0.05
m = lambda x: math.atan(a*x)

def Boxcar(v):
    if v < 1 and v > -1:
        return 0.5
    else:
        return 0

def Gaussian(v):
    return (1/math.sqrt(2*math.pi))*math.exp(-(v**2)/2)

def Epanechnikov(v):
    if v < 1 and v > -1:
        return 0.75*(1-v**2)
    else:
        return 0

def Tricube(v):
    if v < 1 and v > -1:
        return (70/81.0)*((1-abs(v)**3)**3)
    else:
        return 0

def reg(x, Xs, Ys):
    nominator = 0.0
    denominator = 0.0 
    for i in range(len(Xs)):
        nominator += Ys[i]*K((Xs[i]-x)/h_n)
        denominator += K((Xs[i]-x)/h_n)
    return nominator/denominator

values = []
realValues = []
regValues = []
Xs = []

Umin = -2
Umax = 2
step = (Umax - Umin)/float(N)
for i in range(N):
    x = Umin + (i * step)
    z = rand.gauss(0, l**2)
    values.append(m(x)+z)
    realValues.append(m(x))
    Xs.append(x)

for i in range(N):
    print(f'{int(i*100/float(N))}%')
    x = Umin + (i * step)
    regValues.append(reg(x, Xs, values))
plt.plot(Xs, realValues)
plt.plot(Xs, regValues)
plt.show()
