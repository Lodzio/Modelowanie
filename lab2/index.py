import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
FREQ = 104729
N_PROB = 200000

def triang(absx):
    if (absx == 0):
        absx += 0.1312
    
    interval = 1.0/FREQ
    return (absx/interval) - math.floor(absx/interval)

def sin(x):
    return (np.sin(x*FREQ*np.pi*2) + 1) /2 

def f(x):
    if x < 0:
        return x + 1
    if x > 0:
        return -x + 1
    return 0

lastNum = 0.6123
values = []
while len(values) < N_PROB:
    y = triang(lastNum)
    x = (triang(y) * 2) - 1
    lastNum = y
    print(lastNum)
    if f(x) > y:
        values.append(x)

n, bins, patches = plt.hist(values, 160, facecolor='blue', alpha=0.5)
plt.show()