# [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
# Sum of truncatable primes is 748317
# Time: 2.9011 seconds

from time import time
from sympy import isprime

start = time()


def truncatable_prime(num):
    """ Return True is num is a truncatable prime"""
    num = list(str(num))

    if any(i in num for i in '0 4 6 8'.split(' ')):
        return False

    if any(i in num[1:] for i in '2 5'.split(' ')):
        return False

    # left to right and right to left
    for i in range(len(num)):
        # print(num[:i+1])
        # print(num[i:])
        if not isprime(int(''.join(num[:i+1]))):
            return False
        if not isprime(int(''.join(num[i:]))):
            return False

    return True


# print(truncatable_prime(29))
tp = list()
i = 10
while len(tp) < 11:
    i += 1
    if truncatable_prime(i):
        tp.append(i)


print(tp)
print("Sum of truncatable primes is " + str(sum(tp)))

elapsed = (time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")
