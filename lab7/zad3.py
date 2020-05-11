import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand
a = 1
l = 1
N = 500
L = 10
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

def g(x, Xs, Ys): 
    sum = 0.0
    for k in range(L):
        sum += alpha(k, Xs, Ys)*fi(k, x)
    return sum

def f(x, Xs): 
    sum = 0.0
    for k in range(L):
        sum += beta(k, Xs)*fi(k, x)
    return sum

def m_N(x, Xs, Ys):
    fn = f(x, Xs)
    gn = g(x, Xs, Ys)
    if fn == 0:
        return 0
    else :
        return gn/fn

Xs = []
Ys = []

for i in range(N):
    x = (rand.rand() * 2 * math.pi) - math.pi
    z = rand.gauss(0, l**2)
    Xs.append(x)
    Ys.append(m(x)+z)

Umin = -5
Umax = 5
valueN = 100
step = (Umax - Umin)/float(valueN)

xs = []
values = []
est = []
real = []

for i in range(valueN):
    x = Umin + (i * step)
    xs.append(x)
    real.append(m(x))
    est.append(m_N(x, Xs, Ys))

plt.plot(xs, real)
plt.plot(xs, est)
plt.show()
