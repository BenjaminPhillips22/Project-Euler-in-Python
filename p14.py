# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 15:46:16 2016

@author: ben

The Longest Collatz sequence starts at 837799
Time: 8.44 seconds

"""



import time
import math
import numpy

start = time.time()

num = int(1e6)
x = numpy.zeros([num])

for i in range(2, num):
    #print(i)
    n = i
    terms = 0
    while(True):
        if(n<i):
            x[i-1] = x[n-1]+terms
            break
        if(n%2==0):
            n = n/2
        else:
            n = 3*n + 1
        
        terms = terms+1

print("The Longest Collatz sequence starts at " + str(numpy.argmax(x)+1))

elapsed = (time.time() - start)    
print("Time: " + str(round(elapsed,2)) + " seconds")
