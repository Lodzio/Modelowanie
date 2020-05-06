import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand
from multiprocessing import Process, Queue
N = 50000
L = 10
N_f = 100

def F(x, values):
    sum = 0
    for value in values:
        if value <= x:
            sum += 1
    return sum / float(len(values))

def K(v):
    if v < 0.5 and v > -0.5:
        return 1
    else:
        return 0

def estF(x, values, h_n):
    sumK = 0
    for xn in values:
        sumK += K((xn-x)/h_n)
    return (1/(N*h_n))*sumK

valMin = -3 #int(min(values))
valMax = 5 #int(max(values))
step = (valMax - valMin)/float(N_f)

def process(q, h_n):
    values = []
    for i in range(N):
        values.append(rand.gauss(1, 1))
    errSum=0.0
    for i in range(N_f):
        x = (i*step) + valMin
        errSum += (estF(x, values, h_n) - rand.clearGauss(x, 1, 1))**2
    q.put(errSum)

h_ns = []
Ys = [] 
for x in range(15):
    h_n = (x+1) * 0.05
    processes = []
    q = Queue()
    x = f'{int(x/0.15)}%'
    print(x)
    for l in range(L):
        p = Process(target=process, args=(q, h_n))
        p.start()
        processes.append(p)
    errSum = 0.0
    for p in processes:
        p.join()
        errSum+=q.get()
    h_ns.append(h_n)
    Ys.append(errSum/L)
plt.loglog(h_ns, Ys)
plt.show()