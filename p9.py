# Special Pythagorean triplet
# abc is  31875000
# Time: 4.0917 seconds

import time

start = time.time()


def get_abc():
    for a in range(1, 500):
        for b in range(a+1, 500):
            for c in range(b+1, 500):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    print("a:{} b:{} c:{}".format(str(a), str(b), str(c)))
                    return(a*b*c)


print('abc is ' + str(get_abc()))
elapsed = (time.time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")
