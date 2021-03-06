import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from multiprocessing import Process, Queue
import time
import rand

s = 10
L = 100
# N = 100
numOfPoints = 10
maxN = 10000
minN = 30

def getPhi(X):
    result = []
    for xi in range(len(X)):
        newRow = []
        for i in range(len(b)):
            if xi - i >= 0:
                newRow.append(X[xi-i])
            else:
                newRow.append(0)
        result.append(newRow)
    return np.matrix(result)

def estb(phi, b, Z):
    Y = phi.dot(b) + Z
    return ((phi.transpose().dot(phi))**-1).dot(phi.transpose()).dot(Y)

def getErr(b, bEst):
    sum = 0
    for i in range(len(b)):
        sum += (b[i] - bEst[i])**2
    return float(sum)

def singleThread(U, b, q):
        Z = np.matrix([rand.gauss(0, 1) for x in range(N)]).transpose()
        phi = getPhi(U)
        q.put(getErr(b, estb(phi, b, Z)))

b = np.matrix([1 for i in range(s)]).transpose()
err = []
Ns = []

for i in range(numOfPoints):
    N = int(maxN**(i/float(numOfPoints-1)))+minN
    U = [rand.gauss(0, 1) for x in range(N)]
    sum = 0
    processes = []
    q = Queue()
    print(N)
    for i in range(L):
        p = Process(target=singleThread, args=(U, b, q))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
        sum+=q.get()
    err.append(sum/L)
    Ns.append(N)

plt.loglog(Ns, err)
plt.show()
