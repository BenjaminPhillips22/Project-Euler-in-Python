# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 18:38:59 2016

@author: ben

Number of routes: 648
Time: 0.0001 seconds

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

a = math.factorial(100)
a = sum_digits(a)

    
print("Number of routes: " + str(a))

elapsed = (time.time() - start)    
print("Time: " + str(round(elapsed,4)) + " seconds")
