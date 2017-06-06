#Sum of all the positive integers which cannot be written as the sum of two abundant numbers 4179871
#Time: 20.3447 seconds


import time
import os
import numpy as np
import itertools



start = time.time()


def is_abundant(num):
    half_num = int(np.ceil(num/2))
    return np.sum(np.where(num%np.linspace(1,half_num,half_num)==0)[0] + 1) > num
    
abundats = set()
s = 0

for p in range(1, 28123+1):
    if is_abundant(p):
        abundats.add(p)
    if not any( (p-a in abundats) for a in abundats ):
        s+= p

print('Sum of all the positive integers which cannot be written as the sum of two abundant numbers ' + str(s) )
elapsed = (time.time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")