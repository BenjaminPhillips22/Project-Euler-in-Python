#The millionth lexicographic permutation is 2783915460
#Time: 0.0005 seconds

import time
import math

start = time.time()

def nthPerm(s, n):
    if len(s)==1:
        return s
    k = math.factorial(len(s)-1)
    div = n//k
    mod = n%k
    return s[div] + nthPerm(s[:div] + s[div+1:], mod)



print('The millionth lexicographic permutation is ' + str(nthPerm('0123456789', 999999)) )
elapsed = (time.time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")