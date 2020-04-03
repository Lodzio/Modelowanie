import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand
L = 20
miref = 0
sref = 1

def mi(values):
    sum = 0
    for v in values:
        sum += v
    return sum / len(values)

def s2(values):
    sum = 0
    m = mi(values)
    for v in values:
        sum += (v - m)**2
    return sum / len(values)

def S2(values):
    sum = 0
    m = mi(values)
    for v in values:
        sum += (v - m)**2
    return sum / (len(values)-1)

def Err(values, ref):
    sum = 0
    for value in values:
        sum += (value - ref)**2
    return sum / len(values)

def cycle(N, estHandler, estRefValue):
    estValues = []
    for l in range(L):
        values = []
        for i in range(N):
            values.append(rand.gauss(miref, sref))
        estValues.append(estHandler(values))
    return Err(estValues, estRefValue)

# values = []
# Ns = []
# for N in range(1000, 100000, 5000):
#     values.append(cycle(N, mi, miref))
#     Ns.append(N)
#     print(N)
# plt.loglog(Ns, values)
# plt.show()

values = []
for i in range(5000000):
    x = rand.cauchy()
    values.append(x)
plt.hist(values, 400, facecolor='blue', alpha=0.5)
plt.show()