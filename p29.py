# number of terms; 9183
# Time: 0.0118 seconds

from time import time

start = time()

terms = set()

for a in range(2, 101):
    for b in range(2, 101):
        terms.add(a**b)

print("number of terms; " + str(len(terms)))

elapsed = (time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")

# in one line
# len(set(a**b for a in range(2, 101) for b in range(2, 101)))
