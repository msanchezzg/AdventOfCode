#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys


def has_parents(n, parents_list):
    for x in parents_list:
        for y in parents_list:
            if x != y and x+y == n:
                return True

    return False


def main(input_file):
    with open(input_file, 'r') as f:
        lines = [int(x) for x in f.readlines()]

    PREAMBLE = 25       # In the example the preamble is 5
    invalid_number = -1

    # STAR 1: FIND NUMBER THAT DOES NOT HAVE 2 NUMBERS THAT SUM IT IN PREVIOUS RANGE
    print('PART 1')
    for index, n in enumerate(lines[PREAMBLE:]):
        parents_list = lines[index:index+PREAMBLE]
        if not has_parents(n, parents_list):
            invalid_number = n
            print(f'First number that does not have parents in preamble list = {invalid_number}')
            break

    print('\n---------------------------------------------------\n')

    # STAR 2: FIND RANGE OF N NUMBERS THAT SUM INVALID NUMBER FROM STAR 1
    print('PART 2')
    found_numbers = False
    numbers = []
    index_inf = -1
    index_sup = -1
    for index, n in enumerate(lines):
        numbers = [n]
        index_inf = index
        for index2, m in enumerate(lines[index+1:]):
            numbers.append(m)
            if sum(numbers) == invalid_number:
                found_numbers = True
                index_sup = index2 + index + 1
                break
            if sum(numbers) > invalid_number:
                break

        if found_numbers:
            break

    print(f'Numbers that sum {invalid_number}: indeces {index_inf} ({lines[index_inf]}) to {index_sup} ({lines[index_sup]})')
    print(f'Numbers: {numbers}')
    min_n = min(numbers)
    max_n = max(numbers)
    print(f'\nSum of smallest and biggest number = {min_n} + {max_n} = {min_n + max_n}')


if __name__ == "__main__":
    main(sys.argv[1])
