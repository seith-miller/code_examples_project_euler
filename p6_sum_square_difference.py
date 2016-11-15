'''
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
'''

max_num = 100


def sum_of_the_squ():
    my_sum = 0

    for i in range(0, max_num + 1):
        my_sum += i * i

    return my_sum


def square_of_the_sum():
    my_sum = 0

    for i in range(0, max_num + 1):
        my_sum += i

    return my_sum * my_sum

if __name__ == '__main__':
    print(square_of_the_sum() - sum_of_the_squ())
