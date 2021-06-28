#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys


def generator1(start_value, factor):
    x = start_value
    divisor = 2147483647
    while True:
        x *= factor
        x %= divisor
        yield x

def generator2(start_value, factor, multiple=1):
    x = start_value
    divisor = 2147483647
    while True:
        x *= factor
        x %= divisor
        if x % multiple == 0:
            yield x


def star1(start_valueA, start_valueB):
    factorA = 16807
    factorB = 48271
    generatorA = generator1(start_valueA, factorA)
    generatorB = generator1(start_valueB, factorB)

    num_pairs = int(40e6)
    matches = 0
    mask = 0xFFFF
    for i in range(num_pairs):
        # print(i, file=sys.stderr)
        a = next(generatorA) & mask
        b = next(generatorB) & mask
        if a == b:
            matches += 1

    print('PART 1')
    print(f'Number of matches = {matches}')


def star2(start_valueA, start_valueB):
    factorA = 16807
    factorB = 48271
    multipleA = 4
    multipleB = 8
    generatorA = generator2(start_valueA, factorA, multipleA)
    generatorB = generator2(start_valueB, factorB, multipleB)

    num_pairs = int(5e6)
    matches = 0
    mask = 0xFFFF
    for i in range(num_pairs):
        # print(i, file=sys.stderr)
        a = next(generatorA) & mask
        b = next(generatorB) & mask
        if a == b:
            matches += 1

    print('PART 2')
    print(f'Number of matches = {matches}')


def main(input_file):

    with open(input_file, 'r') as f:
        lineA, lineB = f.readlines()

    start_valueA = int(lineA.split()[-1])
    start_valueB = int(lineB.split()[-1])
    star1(start_valueA, start_valueB)
    print('\n--------------------------------------\n')
    star2(start_valueA, start_valueB)


if __name__ == "__main__":
    main(sys.argv[1])
