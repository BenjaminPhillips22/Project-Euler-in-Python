# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?
# sum of diagonal is 669171001
# Time: 0.002 seconds

from time import time

terms = set()

for a in range(2, 101):
    for b in range(2, 101):
        terms.add(a**b)

print("number of terms; " + str(len(terms)))

start = time()
elapsed = (time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")
