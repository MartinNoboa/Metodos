# 
# Quantitative Methods and Simulation
# Script MonteCarlo Simulation
# @author:
#       Eric Torres     -  A01700249  
#       Martin Noboa    -  A01704052
#       Samuel Gonzalez -  A01704696
#       
# @date: 
#       October 4, 2021
# @last_modified:
#       October 4, 2021
#
import numpy as np
import math
import matplotlib.pyplot as plt

#values for MCS
N = int(input('N: '))
a = 0
b = 10
blue_points = 0
#function to integrate
def function(x):
    y = np.sqrt(x)
    return y


linespc = np.linspace(a,b,N)
xc = function(linespc)
yc = function(linespc)

xb = []
yb = []
xr = []
yr = []


for _ in range(N):
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)
    value = function(x)
    if y < value:
        blue_points += 1
        xb.append(x)
        yb.append(y)
    else:
        xr.append(x)
        yr.append(y)
        
        
integral = 0
for i in xb:
    integral += function(i)

areaCurv = (b-a)/float(integral)*N
print(areaCurv) 


plt.plot(xc,yc)
plt.plot(xb,yb,'ob')
plt.plot(xr,yr,'xr')
plt.show()
