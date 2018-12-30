# sum of terms; 443839
# Time: 2.1133 seconds

from time import time

start = time()

power = 5
my_range = 6*(9**5)
terms = []

for i in range(2, my_range):
    if sum([int(j)**5 for j in str(i)]) == i:
        terms.append(i)

print("sum of terms; " + str(sum(terms)))
elapsed = (time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")
