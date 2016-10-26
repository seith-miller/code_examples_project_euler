"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers?
"""

min_num = 100
max_num = 1000
palindrome = []


def find_palendroms():
    product = ''

    for x in range(min_num, max_num):
        for y in range(min_num, max_num):
            product = str(x * y)
            if product == product[::-1]:
                palindrome.append(int(product))


def main():
    find_palendroms()

    palindrome.sort(reverse=True)
    print(palindrome[0])


if __name__ == '__main__':
    main()
