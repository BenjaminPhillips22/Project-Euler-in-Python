#

from time import time
from math import factorial


def sum_of_fact_dig(n):
    digits = list(str(n))
    facts = sum([factorial(int(d)) for d in digits])
    return facts == n


start = time()
sum_facts = []

for i in range(3, 100000):
    if sum_of_fact_dig(i):
        sum_facts.append(i)

print(sum(sum_facts))
print(sum_facts)

elapsed = (time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")

# tests
# print(sum_of_fact_dig(145))
# print(sum_of_fact_dig(146))
