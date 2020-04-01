import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
FREQ = 1231223123
N_PROB = 5000000
seed = 0.6123

def rand():
    global seed
    seed = (seed*FREQ) - math.floor(seed*FREQ)
    return seed

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

def gauss(x):
    return (1/math.sqrt(math.pi*2))*math.exp(-x*x/2)

def randLaplace():
    x = rand()
    if x < 0.5:
        return math.log(2*x)
    if x > 0.5:
        return -math.log(2*(1-x))
    return 0

def laplace(x):
    return 0.5*math.exp(-abs(x))

# values = []
# while len(values) < N_PROB:
#     y = rand()
#     x = (rand() * 2) - 1
#     if f1(x) > y:
#         values.append(x)

# n, bins, patches = plt.hist(values, 500, facecolor='blue', alpha=0.5)
# plt.show()
# start = time.time()
# values = []
# while len(values) < N_PROB:
#     y = rand() * 50
#     x = rand()
#     if f2(x) >= y:
#         values.append(x)
# end = time.time()
# print(end - start)

# n, bins, patches = plt.hist(values, 100, facecolor='blue', alpha=0.5)
# plt.show()

# start = time.time()
# values = []
# while len(values) < N_PROB:
#     y = rand()
#     x = (rand() * 2) - 1
#     if f3(x) > y:
#         values.append(x)
# end = time.time()
# print(end - start)

# n, bins, patches = plt.hist(values, 500, facecolor='blue', alpha=0.5)
# plt.show()

start = time.time()
values = []
while len(values) < N_PROB:
    y = rand()
    x = randLaplace()
    if gauss(x) > laplace(x)*y*2:
        values.append(x)
end = time.time()
print(end - start)

n, bins, patches = plt.hist(values, 500, facecolor='blue', alpha=0.5)
plt.show()