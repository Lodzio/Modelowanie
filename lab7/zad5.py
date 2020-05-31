import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand
from multiprocessing import Process, Queue

a = 1
l = 1
N = 500
Q = 100
def m(x): 
    if abs(x) < 1:
        return a*(x**2)
    elif abs(x) < 2:
        return 1
    else:
        return 0


def fi(k, x):
    if k == 0:
        return math.sqrt(1/(2*math.pi))
    else:
        return math.sqrt(1/math.pi)*math.cos(k*x)

def alpha(k, Xs, Ys):
    sum = 0.0
    for i in range(len(Xs)):
        x = Xs[i]
        y = Ys[i]
        sum += y*fi(k, x)
    return sum/len(Xs)

def beta(k, Xs):
    sum = 0.0
    for i in range(len(Xs)):
        x = Xs[i]
        sum += fi(k, x)
    return sum/len(Xs)

def g(x, Xs, Ys, L): 
    sum = 0.0
    for k in range(L):
        sum += alpha(k, Xs, Ys)*fi(k, x)
    return sum

def f(x, Xs, L): 
    sum = 0.0
    for k in range(L):
        sum += beta(k, Xs)*fi(k, x)
    return sum

def m_N(x, Xs, Ys, L):
    fn = f(x, Xs, L)
    gn = g(x, Xs, Ys, L)
    if fn == 0:
        return 0
    else :
        return gn/fn

def subValid(L, est, real, left, right, queue):
    sum = 0.0
    for q in range(left, right):
        x = (2*q)/Q
        sum += (est(x)-real(x))**2
    queue.put(sum)


def valid(L, est, real):
    sum = 0.0
    threads = 8
    processes = []
    q = Queue()
    for i in range(threads):
        step = 2*Q/threads
        left = int((i * step) - Q)
        right = int((step * (i + 1)) - Q)
#         p = Process(target=subValid, args=(L, est, real, left, right, q))
        subValid(L, est, real, left, right, q)

#         p.start()
#         processes.append(p)

#     for p in processes:
#         p.join()
        sum+=q.get()

    # for q in range(-Q, Q):
    #     x = (2*q)/Q
    #     sum += (est(x)-real(x))**2
    return sum/(2*Q)

Xs = []
Ys = []

for i in range(N):
    x = (rand.rand() * 2 * math.pi) - math.pi
    z = rand.gauss(0, l**2)
    Xs.append(x)
    Ys.append(m(x)+z)

Umin = -Q
Umax = Q
valueN = 100
step = (Umax - Umin)/float(valueN)

error = []
Ls = []

for L in range(1, 50):
    print(L)
    Ls.append(L)
    error.append(valid(L, lambda x: m_N(x, Xs, Ys, L), m))

plt.loglog(Ls, error)
plt.show()