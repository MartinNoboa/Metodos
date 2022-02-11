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

def signsTable(numbers,N):
    signs=[]
    for i in range(N):
        if(i<N-1):
            if(numbers[i]<numbers[i+1]):
                signs.append("+")
            else:
                signs.append("-")
    return signs

def runsTablePositiveSign(signs,numSigns):
    positiveCount=0
    lastSymbol="x"
    for i in range(numSigns):
        if(signs[i]=="+" and lastSymbol !="+"):
           positiveCount+=1
        lastSymbol=signs[i] 
    return positiveCount

def runsTableNegativeSign(signs,numSigns):
    negativeCount=0
    lastSymbol="x"
    for i in range(numSigns):
        if(signs[i]=="-" and lastSymbol !="-"):
           negativeCount+=1
        lastSymbol=signs[i]
    return negativeCount

numbers = []
with open('exp.txt') as file:
    while (line := file.readline().rstrip()):
        numbers.append(float(line))
    file.close()

D=4
N=len(numbers)
signs=signsTable(numbers,N)
plusSign= signs.count('+')
minusSign= signs.count('-')
numSigns=plusSign+minusSign
positiveRuns=runsTablePositiveSign(signs,numSigns)
negativeRuns=runsTableNegativeSign(signs,numSigns)
numberRuns=positiveRuns+negativeRuns
miuValue=((2*numSigns)-1)/3
miuValue= np.round(miuValue,D)
sigmaValue=((16*numSigns)-29)/90
sigmaValue= np.sqrt(sigmaValue)
sigmaValue=np.round(sigmaValue,D)
zScore=np.round((numberRuns-miuValue)/sigmaValue,D)
criticalValue=1.96
print(signs)
print("(+):",plusSign,"  ","(-):",minusSign,"  total:",numSigns)
print("Positive runs: ",positiveRuns)
print("Negative runs: ",negativeRuns)
print("Lambda: ",miuValue)
print("Sigma: ",sigmaValue)
print("Z-Score: ", zScore, "\n")
print("H0: Appereance of the numbers is random \n")
print("H1: Appereance of the numbers is not random \n")
if(zScore<criticalValue):
    print("Since ",zScore," < ",criticalValue, ", H0 is not rejected\n")
else:
    print("Since ",zScore," > ",criticalValue, ", H0 is rejected\n")