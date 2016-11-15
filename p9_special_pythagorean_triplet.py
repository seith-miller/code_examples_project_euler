'''
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import functools

max_num = 1000


def main():
    my_list = []

    # find all the sets of 3 num where a + b + c = 1000
    for c in range(1, max_num):
        for b in range(1, c):
            for a in range(1, b):
                if a + b + c == 1000:
                    # find the set where a^2 + b^2 = c^2
                    if a**2 + b**2 == c**2:
                        my_list = [a, b, c]

    # return a * b * c
    return functools.reduce(lambda x, y: x * y, my_list)


if __name__ == '__main__':
    print(main())
