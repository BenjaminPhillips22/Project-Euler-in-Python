# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 22:38:10 2016
Modified on Wed Oct 11 2017
@author: ben

76576500 is the first triangle number to have over 500 factors
Time: 6.08 seconds

"""

import time
import math


def factors(n):
    result = [i for i in range(1, math.floor(math.sqrt(n))) if n % i == 0]
    return result


start = time.time()

j = 1
num = 0
while True:
    num += j
    j += 1
    if len(factors(num))*2 > 500:
        print(str(num),
              " is the first triangle number to have over 500 factors")
        break

elapsed = (time.time() - start)
print("Time: " + str(round(elapsed, 2)) + " seconds")
