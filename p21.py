# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 18:43:00 2016

@author: ben

[220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]
Number of routes: 31626
Time: 2.6392 seconds


"""



import time
import math
import numpy

start = time.time()



def factors_sum(n):
    result = []
    for i in range(1, math.ceil(n/2)+1):
        if n % i == 0:
            result.append(i)
    #print(result)        
    return sum(result)
    
num = int(1e4)
s = numpy.zeros([num+1])

# store all the factor sums
for i in range(2, num):
    s[i] = factors_sum(i)
    
# find the amicable numbers
ams = []
for i in range(2, num):
    a = i
    b = s[i]
    if( b < num):
        if(s[a] == b):
            if(s[b] == a):
                if(a != b):
                    ams.append(i)
            

print(ams)
print("Number of routes: " + str(sum(ams)))

elapsed = (time.time() - start)    
print("Time: " + str(round(elapsed,4)) + " seconds")
