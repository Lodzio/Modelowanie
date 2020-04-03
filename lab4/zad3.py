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

def sup(distro, refDistro):
    div = []
    for i in range(len(distro)):
        div.append(abs(distro[i] - refDistro[i]))
    return max(div)

def subFromTwox(N):
    values = []
    for i in range(N):
        x = rand.twox()
        values.append(x)

    Fs = []
    Fsref = []
    for i in range(N_Distro):
        x = i/float(N_Distro)
        Fs.append(F(x, values))
        Fsref.append(x**2)
    return sup(Fs, Fsref)

Ns = []
sups = []
for N in range(1000, 100000, 10000):
    subsups = []
    for i in range(10):
        subsups.append(subFromTwox(N))
    Ns.append(N)
    print(N)
    sups.append(sum(subsups)/float(len(subsups)))

plt.plot(Ns, sups)
plt.show()