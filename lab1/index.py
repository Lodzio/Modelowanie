import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
FREQ = 1231223123
N_PROB = 5000000
seed = 0.6123
def rand():
    global seed
    seed = (seed*FREQ) - math.floor(seed*FREQ)
    return seed

def sin():
    global seed
    seed = (np.sin(seed*FREQ*np.pi*2) + 1) /2 
    return seed

def y2(x):
    if x < 0.5:
        return math.sqrt(2*x) - 1
    if x > 0.5:
        return -math.sqrt(2*(1-x))+1 
    return 0

def y3(x): 
    return -math.log(-x+1)

def laplace(x):
    if x < 0.5:
        return math.log(2*x)
    if x > 0.5:
        return -math.log(2*(1-x))
    return 0

# Zadanie 1
values = []
for i in range(0,N_PROB):
    x = sin()
    values.append(math.sqrt(x))
n, bins, patches = plt.hist(values, 500, facecolor='blue', alpha=0.5)
plt.show()

# # Zadanie 2
# values = []
# for i in range(0,N_PROB):
#     x = rand()
#     values.append(y2(x))

# n, bins, patches = plt.hist(values, 500, facecolor='blue', alpha=0.5)
# plt.show()

# # Zadanie 3
# values = []
# for i in range(0,N_PROB):
#     x = rand()
#     values.append(y3(x))

# n, bins, patches = plt.hist(values, 500, facecolor='blue', alpha=0.5)
# plt.show()

# # Zadanie 4
# values = []
# for i in range(0,N_PROB):
#     x = rand()
#     values.append(laplace(x))

# n, bins, patches = plt.hist(values, 500, facecolor='blue', alpha=0.5)
# plt.show()