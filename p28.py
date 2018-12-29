# -*- coding: utf-8 -*-
"""
@author: ben
"""
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?
# sum of diagonal is 669171001
# Time: 0.002 seconds

import time

start = time.time()

corners = [1]
# a 1001*1001 grid is 500 spirals
num_spirals = 500

for s in range(1, num_spirals+1):
    for _ in range(4):
        corners.append(corners[-1] + 2*s)

print("sum of diagonal is " + str(sum(corners)))

elapsed = (time.time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")
