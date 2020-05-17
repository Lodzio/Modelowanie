import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
from multiprocessing import Process, Queue
import rand
D = 1
N = 500
rox = 1
roz = 1
L = 20
mi = np.ones(D)
cov = np.identity(D)*(rox**2)

def f(X, Z, a):
    return X.dot(a)+Z

def MNK(X, Y):
    return ((X.transpose().dot(X))**-1).dot(X.transpose()).dot(Y)

ns = []
err = []
a = np.ones(D)

def model(queue, X, n, a):
    Z = np.array([rand.gauss(0, roz**2) for x in range(n)])
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
print(len(ns), len(err))
plt.loglog(ns, err)
plt.show()