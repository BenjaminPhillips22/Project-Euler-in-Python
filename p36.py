# [0, 1, 3, 5, 7, 9, 33, 99, 313, 585, 717, 7447, 9009, 15351, 32223, 39993, 53235, 53835, 73737, 585585]
# Sum of Double Base Palindromes is 872187
# Time: 1.0155 seconds

from time import time

start = time()


def convert_to_bin(num):
    return "{0:b}".format(num)


def is_palindrome(num):
    word = str(num)
    return word == word[::-1]


# print(is_palindrome(convert_to_bin(585)))

double_base_palindromes = []

for i in range(1000000):
    if is_palindrome(i):
        if is_palindrome(convert_to_bin(i)):
            double_base_palindromes.append(i)

print(double_base_palindromes)
print('Sum of Double Base Palindromes is ' + str(sum(double_base_palindromes)))

elapsed = (time() - start)
print("Time: " + str(round(elapsed, 4)) + " seconds")
