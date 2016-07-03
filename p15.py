# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 16:26:11 2016

@author: ben

Number of routes: 137846528820.0
Time: 0.0 seconds

"""


import time
import math
import numpy

start = time.time()

def calculate_combinations(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))
    
print("Number of routes: " + str(calculate_combinations(40,20)))

elapsed = (time.time() - start)    
print("Time: " + str(round(elapsed,2)) + " seconds")
