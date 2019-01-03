# sum of products: 45228
# Time: 0.3015 seconds

from time import time

start = time()


def pandig(i, j):
    n = i*j
    s = str(i) + str(j) + str(n)
    if len(s) != 9:
        return False
    if '0' in s:
        return False
    if len(set(s)) == 9:
        return True
    else:
        return False


prods = set()
for i in range(0, 100):

    i_len = len(str(i))
    if i_len == 1:
        rg_min = 1000
    elif i_len == 2:
        rg_min = 100
    
    for j in range(rg_min, rg_min*10):
        if (pandig(i, j)):
            n = i*j
            # print('i: {}, j: {}, n: {}'.format(i, j, n))
            prods.add(n)

print('sum of products: ' + str(sum(prods)))

elapsed = (time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")
