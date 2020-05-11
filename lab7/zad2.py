import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand
a = 1
l = 1
N = 2000000
def m(x): 
    if abs(x) < 1:
        return a*(x**2)
    elif abs(x) < 2:
        return 1
    else:
        return 0

Xs = []
Ys = []

for i in range(N):
    x = (rand.rand() * 2 * math.pi) - math.pi
    z = rand.gauss(0, l**2)
    Xs.append(x)
    Ys.append(m(x)+z)
plt.plot(Xs, Ys, ',')
plt.show()
