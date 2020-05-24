import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand
s = 10
N = 100
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

b = np.matrix([1 for i in range(s)]).transpose()
Z = np.matrix([rand.gauss(0, 1) for x in range(N)]).transpose()
U = [rand.gauss(0, 1) for x in range(N)]
phi = getPhi(U)
print(estb(phi, b, Z))
# plt.plot(U, Y)
# plt.show()
