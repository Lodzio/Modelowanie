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
cov = np.identity(D)*(rox**2)

def f(X, Z, a):
    return X.dot(a)+Z

a = np.ones(D)
Z = np.array([rand.gauss(0, roz**2) for x in range(N)])
X = np.matrix([rand.gauss(mi, cov) for x in range(N)])

Y = f(X, Z, a)
print(Y)
