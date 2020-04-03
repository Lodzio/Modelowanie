import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand

N_Distro = 500

def F(x, values):
    sum = 0
    for value in values:
        if value <= x:
            sum += 1
    return sum / float(len(values))

def sup(distro, refDistro):
    div = []
    sum = 0
    for i in range(len(distro)):
        sum += (distro[i] - refDistro[i])**2
        div.append(abs(distro[i] - refDistro[i]))
    return max(div), sum

def subFromTwox(N):
    values = []
    for i in range(N):
        x = rand.twox()
        values.append(x)

    Fs = []
    Fsref = []
    for i in range(N_Distro):
        x = i/float(N_Distro)
        Fs.append(F(x, values))
        Fsref.append(x**2)
    return sup(Fs, Fsref)

file = open("ModelowanieLab4Data.txt", "r") 
values = map(lambda val: float(val), filter(lambda val: val != '',file.read().split('\r\n')))
gauss11 = []
gauss05 = []
cauchy = []
for i in range(50000):
    gauss11.append(rand.gauss(1, 1))
    gauss05.append(rand.gauss(0, 5))
    cauchy.append(rand.cauchy(0, 1.5))

Xs = [] 
distro = []
gauss11Distro = []
gauss05Distro = []
cauchyDistro = []
valMin = -15#int(min(values))
valMax = 15#int(max(values))
step = (valMax - valMin)/float(N_Distro)
for i in range(N_Distro):
    x = (i*step) + valMin
    Xs.append(x)
    distro.append(F(x, values))
    gauss11Distro.append(F(x, gauss11))
    gauss05Distro.append(F(x, gauss05))
    cauchyDistro.append(F(x, cauchy))
    
print(sup(distro, gauss11Distro))
print(sup(distro, gauss05Distro))
print(sup(distro, cauchyDistro))

plt.plot(Xs, distro, 'r')
plt.plot(Xs, gauss11Distro, 'r--')
plt.plot(Xs, gauss05Distro, 'g--')
plt.plot(Xs, cauchyDistro, 'b--')
plt.show()