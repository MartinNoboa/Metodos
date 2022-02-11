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

from os import close, pardir
import matplotlib.pyplot as plt
import numpy as np
import math
import array



def Width(max, min, C):
    wid = (max-min)/ C
    return wid

def Intervals (C,w,d):
    intervals=[]
    intervals.append(0)
    for i in range (int(C)):
        intervals.append(intervals[i]+w)
    intervals=np.round(intervals,d)
    return intervals

def DistTable(numbers,C,intervals,N):
    frequencies=[]
    i=0
    for i in range (int(C)):
        frequencies.append(0)
    for j in range (len(numbers)):
        for i in range (int(C)):
                if(numbers[j] >= intervals[i] and numbers[j] < intervals[i+1]):
                    frequencies[i]=frequencies[i]+1
                elif(numbers[j] >= intervals[i] and i==C):
                    frequencies[i]=frequencies[i]+1
    return frequencies
def squareTable(frequencies,expected,C):
    results=[]
    for i in range(int(C)):
        results.append((np.square(frequencies[i]-expected))/expected)
    return results


numbers = []
with open('data.txt') as file:
    while (line := file.readline().rstrip()):
        numbers.append(float(line))
    file.close()

D=4
C=10
W=0.1
numbers=np.round(numbers,D)
N=len(numbers)
numbers.sort()
intervals=Intervals(C,W,D)
frequencies=DistTable(numbers,C,intervals,N)
expected=N/C
results=squareTable(frequencies,expected,C)
results=np.round(results,D)
total = np.sum(results)
total=np.round(total,D)
## We are always using 10 classes and an alpha of 0.05 so the critical value is goint to be 16.91
criticalValue=16.91
for i in range (int(C)+1):
    if(i<10):
        print("[",intervals[i],"-",intervals[i+1],"]","   ", end='')
        print(frequencies[i],"   ",expected,"   ",results[i])
print("                          X^2=",total,"\n")

print("H0: Generated numbers are not different from the uniform distribution \n")
print("H1: Generated numbers are different from the uniform distribution \n")
if(total<criticalValue):
    print("Since ",total," < ",criticalValue, ", H0 is not rejected\n")
else:
    print("Since ",total," > ",criticalValue, ", H0 is rejected\n")
