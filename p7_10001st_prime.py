'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

max_num = 150000
my_primes = [2]


def is_prime(a):
    return all(a % i for i in range(2, a))


def list_primes():
    for i in range(3, max_num, 2):
        if is_prime(i):
            my_primes.append(i)


if __name__ == '__main__':
    list_primes()

    print(my_primes[10000])
