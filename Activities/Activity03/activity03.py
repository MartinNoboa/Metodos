# 
# Quantitative Methods and Simulation
# Activity 03 - Plotting Frequencies and Histogram
# @author: 
#       Martin Noboa    -  A01704052
#       Eric Torres     -  A01700249 
#       Samuel Gonzalez -  A01704696
#       
# @date: 
#       September 2nd, 2021
# @last_modified:
#       -
#

# modules --------------------------------------------------------------- 
import math as m
import matplotlib.pyplot as plt

values = []
fileName = 'numbers02.txt'

def printData(data):
    """ 
    Print all the data in the array
    @param  -> data as an array of elements 
    @return -> 
    """
    count = 0
    for line in data:
        count += 1
        print(f'line {count}: {line}') 

def getIntervals(w,c,min):
    """ 
    Get the interval based on data
    @param  ->  data as an array of elements 
                w as width
                c as number of classes
    @return -> array of intervals
    """
    intervals=[]
    intervals.append(min)
    for i in range(c):
         intervals.append(intervals[i] + w)
        
    return intervals

def getW(min,max,c):
    """ 
    Get the interval based on data
    @param  ->  min as smallest value in array 
                max as largest value in array
                c as number of classes
    @return -> w
    """
    return (max+min)/c
  
def getFrequencies(values,intervals,n,c): 
    """ 
    Get the frequencies of values in data
    @param  ->  values as an array of elements 
                intervals as array of intervals
                n as number of elements
                c as number of classes
    @return -> array of frequency of values in set intervals
    """
    freq = []
    for i in range (c):
        freq.append(0)
    
    for i in range (n):
        for j in range (c):
            if ( values[i] >= intervals[j] and values[i] < intervals[j+1]):
                freq[j] = freq[j] + 1
            elif ( values[i] >= intervals[j] and c == j ):
                freq[j] = freq[j] + 1
    
    return freq
                
        
         


with open(fileName) as file:
    while (line := file.readline().rstrip()):
        values.append(float(line))
    file.close()
values.sort
    
max = round(max(values),4)
min = round(min(values),4)
n = len(values) 
c = round(1 + 3.333* m.log10(n))
w = round(getW(max,min,c),4)

intervals = getIntervals(w,c,min)
frequencies = getFrequencies(values, intervals, n, c)
# print values of all variables needed

sumFreq = 0;
for i in frequencies:
    sumFreq += i;


print("N = ",n)
print("C = ",c)
print("Max = ",max)
print("Min = ",min)
print("W = ",w)
print("Total freq = ",sumFreq)

# calculated values
print(intervals)
print(frequencies)

#print (sum(frequencies))
classes=[]
list=[]
minLimit = min
for i in range(c) :
    maxLimit=round(minLimit+w-0.0001,4)
    array=[minLimit , maxLimit]
    maxLimit=round(maxLimit+0.0001,4)
    list.append(array)
    string="["+str(minLimit)+"-"+str(maxLimit)+")"
    minLimit=maxLimit
    
    classes.append(string)
    
    
# display histogram
print(classes)
plt.bar(classes, frequencies)
plt.ylabel('Frequencies')
plt.xlabel('Bins')
plt.title('Frequencies of grouped data')
plt.show()

