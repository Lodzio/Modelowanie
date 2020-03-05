import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
FREQ = 1231223123

def triang(absx):
    if (absx == 0):
        absx += 0.1312
    
    interval = 1/FREQ
    return (absx/interval) - math.floor(absx / interval)

def sin(x):
    return (np.sin(x*FREQ*np.pi*2) + 1) /2 

lastNum = 0.6123
values = []
for i in range(0,1500000):
    lastNum = triang(lastNum)
    values.append(lastNum)
n, bins, patches = plt.hist(values, 160, facecolor='blue', alpha=0.5)
plt.show()