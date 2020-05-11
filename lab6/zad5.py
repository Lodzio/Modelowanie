import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
import rand
a = 1
l = 1
N = 500
Q = 100
m = lambda x: math.atan(a*x)

def K(v):
    return (1/math.sqrt(2*math.pi))*math.exp(-(v**2)/2)

def reg(x, Xs, Ys, h_n):
    nominator = 0.0
    denominator = 0.0 
    for i in range(len(Xs)):
        nominator += Ys[i]*K((Xs[i]-x)/h_n)
        denominator += K((Xs[i]-x)/h_n)
    return nominator/denominator

def valid(real, est):
    sum = 0.0
    for q in range(-Q, Q):
        sum += (est(float(q)/Q) - real(float(q)/Q))**2
    return sum/(2*Q)

values = []
realValues = []
error = []
Xs = []
hs = []

Umin = -1
Umax = 1
step = (Umax - Umin)/float(N)
left = 0.02
right = 0.2
for i in range(N):
    x = Umin + (i * step)
    z = rand.gauss(0, l**2)
    values.append(m(x)+z)
    Xs.append(x)
for i in range(1, 25):
    h_n = 0.02 * i
    lambdaReg = lambda x: reg(x, Xs, values, h_n)
    print(f'{int(i*100/float(25))}%')
    error.append(valid(m, lambdaReg))
    hs.append(h_n)


# for looking the best h_n
# while True:
#     h_n = left + ((right-left)/2)
#     lambdaReg = lambda x: reg(x, Xs, values, left)
#     leftErr = valid(m, lambdaReg)
#     lambdaReg = lambda x: reg(x, Xs, values, right)
#     rightErr = valid(m, lambdaReg)
#     if leftErr > rightErr:
#         left = h_n
#     else:
#         right = h_n
#     print(left, right, (leftErr + rightErr)/2)
plt.loglog(hs, error)
plt.show()
