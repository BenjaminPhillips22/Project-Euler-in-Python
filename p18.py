# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 16:50:24 2016

@author: ben
"""
#shortest path is 1074
#Time: 0.0002 seconds

import time

start = time.time()


f = open('p018_triangle.txt')


rr = []
for line in f:
    rr.append([int(i) for i in line.rstrip('\n').split(" ")])
f.close()


for i in range(len(rr)-2,-1,-1 ):
    #print(str(i))
    for j in range(i,-1,-1):
        #print(str(j))
        rr[i][j] += max(rr[i+1][j], rr[i+1][j+1])





print("shortest path is " + str(rr[0][0]))
elapsed = (time.time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")

