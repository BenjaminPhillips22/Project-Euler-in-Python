# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 10:52:19 2016

@author: ben
"""
#Word score total is 871198282
#Time: 0.0408 seconds


import time
import os


os.chdir('/home/ben/python/Euler')

start = time.time()

f = open('p022_names.txt')
words = f.read().replace('"','').split(',')
words.sort()
#print(words)

i=1
word_scores_sum = 0
for w in words:
        
    alph_score = 0
    for char in w:
        alph_score += (ord(char)-64)
    
    word_scores_sum += i*alph_score
    i += 1




print('Word score total is ' + str(word_scores_sum) )
elapsed = (time.time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")