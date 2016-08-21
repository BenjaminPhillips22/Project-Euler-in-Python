# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 17:31:40 2016

@author: ben

"""

#There are 21124 letters
#Time: 0.0026 seconds


import time
import copy

start = time.time()

one_19 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
          'thirteen',
          'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

# print(one_19)

twenty_90 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

one_99 = copy.deepcopy(one_19)

for i in twenty_90:
    for j in one_19[0:10]:
        one_99.append(i + j)

hundred = "hundred"
aand = "and"
onehundred_999 = copy.deepcopy(one_99)


for i in one_19[1:10]:
    for j in one_99:
        if j == "":
            onehundred_999.append(i + hundred)
        else:
            onehundred_999.append(i + hundred + aand + j)


onehundred_999.append("onethousand")

allLetters = ''
for word in onehundred_999:
    allLetters += word



print("There are " + str(len(allLetters)) + " letters")
elapsed = (time.time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")
