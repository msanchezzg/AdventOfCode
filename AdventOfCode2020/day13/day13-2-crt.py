#!/usr/bin/python3
#-*- coding: utf-8 -*-

'''
Functions chinese_remainder and mul_inv used from
https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
'''

import sys

from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    _, buses = lines
    buses = buses.replace('x', '1')
    buses = [int(x) for x in buses.split(',') if x.isdigit()]

    remainders = []
    modulos = []

    for i1, b1 in enumerate(buses):
        if b1 == 1:
            continue
        remainders.append(b1 - i1)       # If done this way, the solution is already minimal
        # remainders.append(i1)
        modulos.append(b1)

    solution = chinese_remainder(modulos, remainders)
    # primes_lcm = reduce(lambda x,y: x*y, buses)
    # minimal_solution = primes_lcm % solution

    print('PART 2')
    print(f'Solution: {solution}')


if __name__ == "__main__":
    main(sys.argv[1])
