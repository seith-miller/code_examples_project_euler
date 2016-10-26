'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''

max_num = 1000000000
max_fact = 18
facts = [7, 9, 11, 13, 15, 16, 17, 19, 20]
i = 20


def divides_evenly(x, y):
    if x % y == 0:
        return True
    else:
        return False


def all_divides_evenly(num_to_check):
    if all(divides_evenly(num_to_check, i) for i in facts):
        return True
    else:
        return False


def check_all_num():
    for i in range(20, max_num, 20):
        if all_divides_evenly(i):
            return i


if __name__ == '__main__':
    print(check_all_num())
