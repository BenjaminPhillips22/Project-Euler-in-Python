#

from time import time
from sympy import primerange

start = time()


def get_rotations(num):
    "returns the rotations as a list of ints"
    rotations = []
    for i in range(len(str(num))):
        rotations.append(int(str(num)[i:] + str(num)[0:i]))
    return rotations


circular_prime_set = set()
checked_number_set = set()

primes = list(primerange(0, 1e6))

even_digits = set(['0 2 4 5 6 8'])

odd_digit_primes = [p for p in primes if len(set(list(str(p))).intersection(even_digits)) == 0]

a = sum(all(pr in odd_digit_primes for pr in get_rotations(p)) for p in odd_digit_primes)

print("There are ", a, " circular primes")

elapsed = (time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")
