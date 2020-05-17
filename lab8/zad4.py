import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand
D = 100
N = 500
mi = np.ones(D)
rox = 1
roz = 1
cov = np.identity(D)*(rox**2)

def f(X, Z, a):
    return X.dot(a)+Z

def MNK(X, Y):
    return ((X.transpose().dot(X))**-1).dot(X.transpose()).dot(Y)

a = np.ones(D)
Z = np.array([rand.gauss(0, roz**2) for x in range(N)])
X = np.matrix([rand.gauss(mi, cov) for x in range(N)])
Y = f(X, Z, a).transpose()
var = roz**2*(X.transpose().dot(X))**-1

plt.imshow(var, extent=[0,100,0,1], aspect='auto')
plt.show()