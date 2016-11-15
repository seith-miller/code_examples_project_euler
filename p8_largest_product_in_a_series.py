'''
Largest product in a series
Problem 8

The four adjacent digits in the 1000-digit number
that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number
that have the greatest product.

What is the value of this product?
'''

import functools

big_num = '''73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'''

big_list = []

num_of_adj_dig = 13

running_high = 0


def fill_big_list(my_str):
    # turn big_num into a list of int
    for i in my_str:
        big_list.append(int(i))


def make_sub_list(key):
        # make a sublist of digits in
        sub_list = []

        for i in range(num_of_adj_dig):
            sub_list.append(big_list[key + i])

        return sub_list


def mult_list(my_list):
    # return the product of all the digits in my_list
    return functools.reduce(lambda x, y: x * y, my_list)


def tick_through():
    # tick through all the starting digits in big_num_list - 1 num_of_adj_dig

    my_high = running_high

    for i in range(0, len(big_list) + 1 - num_of_adj_dig):
        product = mult_list(make_sub_list(i))

        # if the product is grater then running_high set it to running_high
        if product > my_high:
            my_high = product

    print(my_high)


if __name__ == '__main__':
    fill_big_list(big_num)
    tick_through()
