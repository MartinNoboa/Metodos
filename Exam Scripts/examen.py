# 
# Quantitative Methods and Simulation
# Script for final exam
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
import random as rnd
import matplotlib.pyplot as plt
import numpy as np

def gen_exp(N, lam):
    numbers = []
    for _ in range(N):
        R = rnd.random()
        x = np.log(R)/lam
        numbers.append(x)
    return numbers


def gen_triangular(N,a,b,c):
    numbers = []
    for _ in range(N):
        R = rnd.random()
        cut = (c - a)/(b - a)
        if 0 <= R <= cut:
            x = a + np.sqrt(R*(b - a)*(c - a))
        else:
            x = b - np.sqrt((1 - R)*(b - a)*(b - c))
        numbers.append(x)
    return numbers


def genweibull(N, alpha, beta):
    numbers = []
    for _ in range(N):
        R = rnd.random()
        x = alpha (-np.log(R))*(1/beta)
        numbers.append(x)
    np.savetxt('data.txt', numbers, delimiter=',')
    return numbers

##Normal
def gen_normal(N, miu, sigma):
    U1 = np.random.rand(N)
    U2 = np.random.rand(N)
    x = miu + sigma * np.sqrt(-2 * np.log(U1)) * np.cos(2 * np.pi * U2)
    return x


def examen(N,a,b,c):
    numbers = []
    for _ in range(N):
        R = rnd.random()
        if 0 <= R < a:
            x = 2 * np.sqrt(R*10/3) - 2
        elif a <= R < b:
            x = (R - 0.3) / 0.3
        elif b <= R < c:
            x = 3 - (4 / 3 * np.sqrt(5 - 5*R))

        numbers.append(x)
    return numbers


num = gen_exp(10000,100)
np.savetxt('exp.txt',num,delimiter=',')