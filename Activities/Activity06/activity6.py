# 
# Quantitative Methods and Simulation
# Script Poisson random numbers accepted and reject values
# @author:
#       Eric Torres     -  A01700249  
#       Martin Noboa    -  A01704052
#       Samuel Gonzalez -  A01704696
#       
# @date: 
#       October 10, 2021
# @last_modified:
#       October 10, 2021
#

import numpy as np
import math
from math import e
import matplotlib.pyplot as plt
from numpy import random

def factorial(n):
    ans = 1
    for i in range (1, n+1):
        ans = ans * i
    return ans    

def valores (alpha, N, numbers):
    for i in range (N):
        numbers.append((pow(alpha, i)*(pow(e, -alpha)))/factorial(i))
    return numbers

N = int(input('N: '))
a = float(input('Alpha: '))
numbers = []
accepted =[]
rejected=[]
cutting_point = pow(e, -a)
print("Cutting point: ",cutting_point)
result = valores(a, N,numbers)
print("List of complete random values: ",result)
P=1

for i in range(N):
    aux=numbers[i]*P
    if(aux<cutting_point):
        accepted.append(numbers[i])
    else:
        rejected.append(numbers[i])
        P=aux

print("Accepted numbers: ",accepted)
print("Rejected numbers: ",rejected)

