import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from multiprocessing import Process, Queue
import time
import rand
D = 1
N = 100
mi = np.ones(D)
rox = 1
roz = 1
roe = 1
b1 = 0.5
L=20
cov = np.identity(D)*(rox**2)
def createZ():
    e = np.array([rand.gauss(0, roe**2) for x in range(-2, N)])
    Z = []
    for I in range(N):
        i = I + 2
        Z.append(e[i] + (b1*e[i-1]))
    return np.matrix(Z)

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

ns = []
err = []
a = np.ones(D)

def model(queue, X, n, a):
    Z = createZ()
    Y = f(X, Z, a).transpose()
    queue.put(float((MNK(X, Y) - a)**2))

numOfPoints = 10
maxN = 100000
for i in range(numOfPoints):
    N = int(maxN**(i/float(numOfPoints-1)))
    print(N)
    X = np.matrix([rand.gauss(mi, cov) for x in range(N)])
    error = 0
    processes = []
    q = Queue()
        
    for i in range(L):
        p = Process(target=model, args=(q, X, N, a))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
        error+=q.get()
    err.append(error/L)
    ns.append(N)
plt.loglog(ns, err)
plt.show()