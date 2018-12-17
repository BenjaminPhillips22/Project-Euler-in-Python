# -*- coding: utf-8 -*-
"""
@author: ben
"""
# n = 71, a = -61, b = 971 and a*b = -59231
# Time: 5.3751 seconds

import time
from sympy import isprime
from sympy import primerange

start = time.time()

b_list = list(primerange(0, 1000))
our_primes = b_list.copy()


def ab_tester(a, b):
    """
    Returns the maximum number of primes for consecutive
    values of n, starting with n=0, for these a and b.
    """
    n = 0
    while True:
        y = n**2 + a*n + b
        
        if y in our_primes:
            n += 1
            continue
        
        if isprime(y):
            our_primes.append(y)
            n += 1
            continue
        
        return n


best = {'a': 0, 'b': 0, 'n': 0}
for a in range(-999, 1000):
    for b in b_list:
        n = ab_tester(a, b)
        if n > best['n']:
            best['a'] = a
            best['b'] = b
            best['n'] = n

print('n = ' + str(best['n']) + ', a = ' +
      str(best['a']) + ', b = ' + str(best['b']) +
      ' and a*b = ' + str(best['a']*best['b']))

elapsed = (time.time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")
