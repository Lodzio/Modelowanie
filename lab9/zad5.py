import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand
D = 2
N = 100
mi = np.ones(D)
rox = 1
roz = 1
roe = 1
b1 = 0.5
cov = np.identity(D)*(rox**2)
def createZ():
    e = np.array([rand.gauss(0, roe**2) for x in range(-2, N)])
    Z = []
    for I in range(N):
        i = I + 2
        Z.append(e[i] + (b1*e[i-1]))
    return np.matrix(Z).transpose()

def f(X, Z, a):
    return X.dot(a)+Z

def MNK(X, Y):
    return ((X.transpose().dot(X))**-1).dot(X.transpose()).dot(Y)

def createR(Z):
    R = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if abs(i - j) == 0:
                R[i, j] = 1
            elif abs(i - j) == 1:
                R[i, j] = 0.5
    return R

a = np.ones(D)
X = np.matrix([rand.gauss(mi, cov) for x in range(N)])
Z = createZ()
Y = f(X, Z, a).transpose()
R = createR(Z)
plt.imshow(R, extent=[0,100,0,100], aspect='auto')
plt.show()