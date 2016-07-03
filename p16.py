# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 16:40:58 2016

@author: ben

Number of routes: 1366
Time: 0.0 seconds

"""



import time
import math
import numpy

start = time.time()

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

a = 2**1000
a = sum_digits(a)

    
print("Number of routes: " + str(a))

elapsed = (time.time() - start)    
print("Time: " + str(round(elapsed,2)) + " seconds")
