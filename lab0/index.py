import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
FREQ = 1231223123
m = 100000
c = 10
lastXes = [0.6123]
ases = [3, 1, -4, 2, 5, 8]

def triang(absx):
    return (absx*FREQ) - math.floor(absx*FREQ)

def sin(x):
    return (np.sin(x*FREQ*np.pi*2) + 1) /2 

def zad3(): 
    newX = 0
    for i in range(len(ases)):
        if i >= len(lastXes):
            continue
        a = ases[i]
        x = lastXes[i]
        newX += a*x
    newX += c
    newX %= m
    if len(lastXes) == len(ases):
        for i in range(len(lastXes) - 1):
            lastXes[i] = lastXes[i + 1] 
        lastXes[len(lastXes) -1] = newX
    else:
        lastXes.append(newX)
    return newX

def powtorzenia(values):
    for i in range(0, (len(values)/50000) ):
        try:
            result1 = values[i + 1:len(values)].index(values[i])
            result2 = values[i + 2:len(values)].index(values[i + 1])
            if result1 != ValueError and result2 != ValueError:
                return result1
        except:
              print("checking ", i/(len(values)/50000.0)) 
    return(-1)

lastNum = 0.6123
values = []
# x=[]
for i in range(0,5000000):
    lastNum = zad3()
    values.append(lastNum)
print(powtorzenia(values))
# for i in range(0,1000):
#     values.append(sin(i/1000.0))
#     x.append(i/1000.0)
n, bins, patches = plt.hist(values, 160, facecolor='blue', alpha=0.5)
# plt.plot(x, values)
plt.show()