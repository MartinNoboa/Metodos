# 
# Quantitative Methods and Simulation
# Activity 04 - Uniform random numbers and randomness tests
# @author:
#       Eric Torres     -  A01700249  
#       Martin Noboa    -  A01704052
#       Samuel Gonzalez -  A01704696
#       
# @date: 
#       September 19, 2021
# @last_modified:
#       -
#
import numpy as np

def linearCongruentialMethod(Xo, m, a, c,noOfRandomNums):
    r=[0] * (noOfRandomNums)
    for i in range( noOfRandomNums):
        xNext=((Xo*a)+c)%m
        r[i] = xNext/m
        Xo=xNext
    np.savetxt('data.txt', r, delimiter=',')
    return r

    
Xo = 88
m = 100
a = 50
c = 2
noOfRandomNums = 1000
randomNums = [0] * (noOfRandomNums)


r=linearCongruentialMethod(Xo, m, a, c,noOfRandomNums)
print(r)


