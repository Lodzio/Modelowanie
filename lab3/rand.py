import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time
FREQ = 1231223123
N_PROB = 5000000
seed = 0.6123

def rand():
    global seed
    seed = (seed*FREQ) - math.floor(seed*FREQ)
    return seed

def clearGauss(x, m, l):
    return (1/(math.sqrt(math.pi*2*l)))*math.exp(-(x - m)**2/(2*l))

def clearLaplace(x, m, l):
    return (1/2.0*l)*math.exp(-abs(x - m)/l)

def laplace(m, l):
    x = rand()
    if x < 0.5:
        return (math.log(2*x)*l)+m
    if x > 0.5:
        return -(math.log(2*(1-x))*l)+m
    return 0

def gauss(m = 0, l = 1):
    while True:
        y = rand()
        x = laplace(m, l)
        if clearGauss(x, m, l) > clearLaplace(x, m, l)*y*2:
            return x

def cauchy(m = 0, l = 1):
    x = ((rand()-0.5)*0.9)+0.5
    return (l*math.tan(math.pi*(x - 0.5))) + m