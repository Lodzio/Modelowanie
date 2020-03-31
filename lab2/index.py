import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
FREQ = 9797979791
N_PROB = 200000
lastNum = 0.6123

def rand():
    global lastNum
    interval = 1.0/FREQ
    lastNum = (lastNum/interval) - math.floor(lastNum/interval)
    return lastNum

def sin(x):
    return (np.sin(x*FREQ*np.pi*2) + 1) /2 

def f1(x):
    if x < 0:
        return x + 1
    if x > 0:
        return -x + 1
    return 0

def f2(x):
    c = 0.5 * 100/99
    if x < 1/100.0:
        return 50
    if x >= 1/100.0:
        return c
    return 0

def f3(x):
    alpha = np.arccos(x)    
    y = np.sin(alpha)
    return y

values = []
while len(values) < N_PROB:
    y = rand()
    x = (rand() * 2) - 1
    if f1(x) > y:
        values.append(x)

n, bins, patches = plt.hist(values, 160, facecolor='blue', alpha=0.5)
plt.show()

values = []
while len(values) < N_PROB:
    y = rand() * 60
    x = rand()
    if f2(x) > y:
        values.append(x)


n, bins, patches = plt.hist(values, 100, facecolor='blue', alpha=0.5)
plt.show()
values = []
while len(values) < N_PROB:
    y = rand()
    x = (rand() * 2) - 1
    if f3(x) > y:
        values.append(x)


n, bins, patches = plt.hist(values, 100, facecolor='blue', alpha=0.5)
plt.show()