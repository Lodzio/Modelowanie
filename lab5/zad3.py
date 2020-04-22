import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand
N = 500000
N_f = 200
h_n = 0.05

def F(x, values):
    sum = 0
    for value in values:
        if value <= x:
            sum += 1
    return sum / float(len(values))

def K(v):
    if v < 0.5 and v > -0.5:
        return 1
    else:
        return 0

def Boxcar(v):
    if v < 1 and v > -1:
        return 0.5
    else:
        return 0

def estF(x, values):
    sumK = 0
    for xn in values:
        sumK += K((xn-x)/h_n)
    return (1/(N*h_n))*sumK

values = []
for i in range(N):
    values.append(rand.gauss(0, 1))

valMin = int(min(values))
valMax = int(max(values))
step = (valMax - valMin)/float(N_f)
Xs = []
Ys = [] 
for i in range(N_f):
    x = (i*step) + valMin
    Xs.append(x)
    Ys.append(estF(x, values))
plt.plot(Xs, Ys)
plt.show()