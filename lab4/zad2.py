import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand

N_Distro = 100

def F(x, values):
    sum = 0
    for value in values:
        if value <= x:
            sum += 1
    return sum / float(len(values))

values = []
for i in range(500000):
    values.append(rand.twox())

Xs = [] 
distro = []
for i in range(N_Distro):
    x = i/float(N_Distro)
    distrox = F(x, values)
    Xs.append(x)
    distro.append(distrox)
plt.plot(Xs, distro)
plt.show()