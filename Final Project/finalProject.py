# 
# Quantitative Methods and Simulation
# Final Project -  Stochastic Matrices
# @author:
#       Martin Noboa    -  A01704052
#       
# @date: 
#       November 26, 2021
# @last_modified:
#       November 24, 2021
#

# Matrix input
# User created input - validate matrix
# User created file - validate matrix
# Program created - randomize 
# Calculate the long-term state (steady) of the matrix.  (if there is no steady state notify the user)
# Identify if the matrix is regular or not.

from os.path import exists
from numpy.linalg import matrix_power as mp
import numpy as np
import sys
import random


# PRGRAM VARIABLES ###############################################################################
# number of CLI flags 
numberFlags = len(sys.argv)
# number of CLI flags 
flag = sys.argv[1]


###################################################################################################
# FUNCTIONS
###################################################################################################

# PRGRAM FUNCTIONS ################################################################################
# Menu
def menu():
    print("-------------------------------------------------")
    print("Choose what opertation you would like to perform.")
    print("1. Print matrix.")
    print("2. Calculate the probability from going to one state to another in x number of steps.")
    print("3. Calculate the long-term state (steady) of the matrix.")
    print("4. Verify the matrix is stochastic.")
    print("5. Verify the matrix is regular.")

# Validate flag and CLI inputs
def validate():
    matrix = []
    if(flag == '-f'):
        if(numberFlags < 3):
            print('No file found.')
            exit()
        else:
            fileName = sys.argv[2]
            if (exists(fileName)):
                matrix = np.loadtxt(fileName, dtype='f', delimiter=',')
            else:
                print("The file does not exist.")
                exit()
    elif(flag == '-i'):
            matrix = getMatrix()
    elif(flag == '-g'):
            matrix = generateMatrix()
    else:
        print("Not a valid flag.")
        exit()
    return matrix

# Loop
def start():
    # user input for opertation
    #declaration of matrix
    matrix = validate()
    option = 1
    while option != 0:
        menu()
        option = int(input("Enter selection number: "))
        if(option == 1):
            printMatrix(matrix)
        elif(option == 2):
            probability(matrix)
        elif(option == 3):
            longTerm(matrix)
        elif(option == 4):
            result = getResult(isStochastic(matrix))
            printResult(result,'s')
        elif(option == 5):
            result = getResult(isRegular(matrix))
            printResult(result,'r')
        else:
            print()


# MATRIXES FUNCTIONS ##############################################################################
# Print matrix
def printMatrix(matrix):
    """Print matrix.
    Receives square matrix to print and size.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end = " ")
        print()

# Get matrix inpur from user
def getMatrix():
    """Get matrix values from user.
    Recieves N value for size of square matrix.
    """
    n = int(input("Enter the size of the matrix: "))
    matrix = []
    print("Enter each row at the time separated by single space: ")
    for i in range(n):
    # taking row input from the user
        row = list(map(float, input().split()))
    # appending the 'row' to the 'matrix'
        matrix.append(row)
    return matrix
              
# Generate random stochastic matrix
def generateMatrix() :
    """Generate an stochastic matrix of size NxN.
    """
    n = 3
    precision = 1000
    matrix = []
    for l in range(n) :
        lineLst = []
        sum = 0
        crtPrec = precision
        for i in range(n-1) :
            val = random.randrange(crtPrec)
            sum += val
            lineLst.append(float(val)/precision)
            crtPrec -= val
        lineLst.append(float(precision - sum)/precision)
        matrix.append(lineLst)
    return matrix


# MATRIXES VALIDATION ############################################################################
# Validate matrix is stochastic
def isStochastic(matrix):
    """Validates the matrix is stochastic.
    Recieves matrix to validate.
    """
    stochastic = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[i][j]
            #print(sum)
        if(sum == 1.0):
            stochastic.append(True)
        else:
            stochastic.append(False)
    return stochastic
      
# Validate if matrix is regular
def isRegular(matrix):
    """Validates the matrix is stochastic.
    Recieves matrix to validate.
    """  
    regular = []
    stochastic = getResult(isStochastic(matrix))
    print(stochastic)
    if(stochastic):
        for i in range(1,7,1):
            aux = arePositive(mp(matrix,i))
            regular.append(aux)
    else:
        regular.append(False)
    return regular

# Helper function. Determines if all values of matrix are nonzero and positive
def arePositive(matrix):
    """Determines if all values of matrix are nonzero and positive.
    Recieves matrix to validate.
    Returns True or False value
    """  
    aux = True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i][j] == 0 or matrix[i][j] < 0):
                aux = False
                break
    return aux
                
# Helper function. Receives array with booleans and prints result
def getResult(matrix):
    counter = 0
    for i in range (len(matrix)):
            if(matrix[i] == True):
                counter+=1
    if (counter == len(matrix)):
        result = True
    else:
        result = False
    return result
    
# Helper function. Receives matrix with booleans and prints result
def printResult(result, case):
    # isStochastic result
    if(case == 's'):
        if(result):
            print("The matrix is stochastic.")
        else:
            print("The matrix is not stochastic.")
    # isRegular result
    elif(case == 'r'):
        if(result):
            print("The matrix is regular.")
        else:
            print("The matrix is not regular.")
            
def probability(matrix):
    noInput = True
    while(noInput):
        x = int(input("Enter the number of steps: "))
        if(x < 0):
            print("The number of steps must be greater than 0.")
        else:
            noInput = False
    for i in range(1,x+1,1):
        print("Step " + str(i) + ":")
        aux = mp(matrix,i)
        printMatrix(aux)
        
def longTerm(matrix):
    aux = mp(matrix,25)
    printMatrix(aux)
    
    
    
    
###################################################################################################
# Main
###################################################################################################
start()
    

