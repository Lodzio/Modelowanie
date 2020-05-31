import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
# from multiprocessing import Process, Queue
import time
import rand

s = 10
L = 100
# N = 100
numOfPoints = 10
maxN = 1000
minN = 30
alpha=0.5

def getR(N):
    matrix = []
    for i in range(N):
        row=[]
        for j in range(N):
            value = 0
            if i == j:
                value = (1+alpha**2)
            elif abs(i - j) == 1:
                value = alpha
            row.append(value)
        matrix.append(row)
    return np.matrix(matrix)
print(getR(10))
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
    R = getR(len(Z))
    Y = phi.dot(b) + Z
    return ((phi.transpose().dot(R**-1).dot(phi))**-1).dot(phi.transpose()).dot(R**-1).dot(Y)

def getErr(b, bEst):
    sum = 0
    for i in range(len(b)):
        sum += (b[i] - bEst[i])**2
    return float(sum)

def getZ(N):
    Z = [rand.gauss(0, 1) for x in range(N)]
    newZ = []
    for i in range(N):
        newZ.append(Z[i] if i == 0 else Z[i] + alpha*Z[i-1])
    return np.matrix(newZ).transpose()

def singleThread(U, b):
        Z=getZ(N)
        phi = getPhi(U)
        return getErr(b, estb(phi, b, Z))

b = np.matrix([1 for i in range(s)]).transpose()
err = []
Ns = []

for i in range(numOfPoints):
    N = int(maxN**(i/float(numOfPoints-1)))+minN
    U = [rand.gauss(0, 1) for x in range(N)]
    sum = 0
    processes = []
#     q = Queue()
    print(N)
    for i in range(L):
        sum += singleThread(U, b)
#         sum+=q.get()
#         p.start()
#         processes.append(p)

#     for p in processes:
#         p.join()
    err.append(sum/L)
    Ns.append(N)

plt.loglog(Ns, err)
plt.show()
