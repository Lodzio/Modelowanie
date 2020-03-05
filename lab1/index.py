import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
FREQ = 1231223123
N_PROB = 50000

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


def triang(absx):
    if (absx == 0):
        absx += 0.1312
    
    interval = 1/FREQ
    return (absx/interval) - math.floor(absx / interval)

def sin(x):
    return (np.sin(x*FREQ*np.pi*2) + 1) /2 

def y(x):
    if x < 0:
        return -math.sqrt(-2*x) + 1
    if x > 0:
        return math.sqrt(2*(1-x))+1 
    return 0
def distro(x):
    if x < -1:
        return 0
    if x < 0:
        return (x**2)/2 + x + (1/2)
    elif x < 1 and x < 1:
        return -(x**2)/2 + x + (1/2)
    return 1


# lastNum = 0.6123
# values = []
# for i in range(0,N_PROB):
#     lastNum = triang(lastNum)
#     values.append(math.sqrt(lastNum))
# n, bins, patches = plt.hist(values, 160, facecolor='blue', alpha=0.5)
# plt.show()
distroVal = []
values = []

for i in range(0,N_PROB):
    # distroVal.append(distro((i/N_PROB)*2-1))
    print(y(((i/N_PROB)*2)-1))

    values.append(y(((i/N_PROB)*2)-1))

# plt.plot((np.asfarray(range(0,N_PROB))/N_PROB*2) -1, distroVal)
n, bins, patches = plt.hist(values, 50, facecolor='blue', alpha=0.5)

plt.show()
# distroVal = np.asfarray(distroVal)
# for i in distroVal:
#     lastNum = triang(lastNum)
#     idx = (np.abs(distroVal - lastNum)).argmin()
    # print(idx)
    # val = find_nearest(distroVal, ((lastNum*2)-1)/distroVal*2-1)
#     values.append((idx/N_PROB*2)-1)

# n, bins, patches = plt.hist(values, 50, facecolor='blue', alpha=0.5)
# plt.show()