import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand
D = 2
N = 10
mi = np.ones(D)
rox = 1
roz = 1
roe = 1
b = 0.5
cov = np.identity(D)*(rox**2)
def Zgenerator():
    e = np.array([rand.gauss(0, roe**2) for x in range(N)])
    Z = [e[0]]
    for i in range(1, N):
        Z.append(e[i] + (b*e[i-1]))
    return Z

def f(X, Z, a):
    return X.dot(a)+Z

a = np.ones(D)
X = np.matrix([rand.gauss(mi, cov) for x in range(N)])
Z = Zgenerator()
Y = f(X, Z, a)
print(Y)
