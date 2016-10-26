"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

num = 600851475143
factors = [1]

for i in range(1, num):
    if num % i == 0:
        factors.append(i)
        num = num / i

        if num == 1:
            break

print(factors[-1])
