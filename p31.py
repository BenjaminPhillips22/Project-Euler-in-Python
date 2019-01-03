# ways: 73682
# Time: 0.002 seconds

from time import time

start = time()

coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200
memo = {}


def ways(target, avc):
    if avc <= 1:
        return 1
    t = target
    if (t, avc) in memo:
        return memo[(t, avc)]
    res = 0
    while target >= 0:
        res += ways(target, avc-1)
        target -= coins[avc-1]
    memo[(t, avc)] = res
    return res


print('ways: ' + str(ways(amount, 8)))

elapsed = (time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")
