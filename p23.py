#Sum of all the positive integers which cannot be written as the sum of two abundant numbers 4179871
#Time: 39.1223 seconds



import time
import os
import numpy as np
import itertools



start = time.time()


potentials = np.arange(12,28123)

def is_abundant(num):
    half_num = int(np.ceil(num/2))
    return np.sum(np.where(num%np.linspace(1,half_num,half_num)==0)[0] + 1) > num
    

# make a vectorized version on the function
is_abundant_vectorize = np.vectorize(is_abundant)

abundants = potentials[is_abundant_vectorize(potentials)]

sum_of_abundant_pairs = list()

for i in range(0, len(abundants)):
    for j in range(i, len(abundants)):
        asum = sum([abundants[i], abundants[j]])
        if asum < 28123:
            sum_of_abundant_pairs.append(asum)
        else:
            break


sum_of_abundant_pairs = np.unique(sum_of_abundant_pairs)

# which number is this are not in the sum_of_abundant_pairs array
aseq = np.arange(1,28123)
not_sum_pf_abundant_pairs = aseq[~np.in1d(aseq, sum_of_abundant_pairs)]

answer = sum(not_sum_pf_abundant_pairs)

print('Sum of all the positive integers which cannot be written as the sum of two abundant numbers ' + str(answer) )
elapsed = (time.time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")