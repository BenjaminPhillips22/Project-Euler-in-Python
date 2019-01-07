# 16 / 64
# 19 / 95
# 26 / 65
# 49 / 98
# Product of fractions is: 0.010000000000000002
# Time: 0.0013 seconds

from time import time

start = time()
product = 1

for n in range(1, 10):
    for d in range(n+1, 10):
        f1 = n/d
        for i in range(1, 10):
            n_1 = []
            n_1.append(i*10 + n)
            n_1.append(n*10 + i)
            d_1 = []
            d_1.append(i*10 + d)
            d_1.append(d*10 + i)
            for l in n_1:
                for k in d_1:
                    if l/k == f1:
                        print(l, '/', k)
                        product *= f1

print("Product of fractions is: " + str(product))
elapsed = (time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")
