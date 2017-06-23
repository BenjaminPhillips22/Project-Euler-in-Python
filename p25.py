#The index of the first term in the Fibonacci sequence to contain 1000 digits is 4782
#Time: 0.0615 seconds

import time

start = time.time()

f1 = 1
f2 = 1

for i in range(1000000):
    f3 = f2 + f1
    f1 = f2
    f2 = f3
    #print(f3)
    if len(str(f3))>=1000:
        break

print('The index of the first term in the Fibonacci sequence to contain 1000 digits is ' + str(i+3) )
elapsed = (time.time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")