import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand

N_Distro = 500

def F(x, values):
    sum = 0
    for value in values:
        if value <= x:
            sum += 1
    return sum / float(len(values))

values = []
for i in range(50000):
    values.append(rand.gauss(0, 1))

Xs = [] 
distro = []
var = []
valMin = int(min(values))
valMax = int(max(values))
step = (valMax - valMin)/float(N_Distro)
for i in range(N_Distro):
    x = (i*step) + valMin
    Xs.append(x)
    f = F(x, values)
    distro.append(f)
for dis in distro:
    var.append(dis*(1-dis)/float(len(distro)))
plt.plot(Xs, var)
# plt.plot(Xs, distro)
plt.show()