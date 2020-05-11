import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand
a = 1
l = 1
N = 20000
m = lambda x: math.atan(a*x)

values = []
Xs = []

Umin = -2
Umax = 2
step = (Umax - Umin)/float(N)
for i in range(N):
    x = Umin + (i * step)
    z = rand.gauss(0, l**2)
    values.append(m(x)+z)
    Xs.append(x)
plt.plot(Xs, values)
plt.show()
