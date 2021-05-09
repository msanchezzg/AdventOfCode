#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys

from functools import reduce


def main(input_file):
    with open(input_file, 'r') as f:
        lines = [int(x) for x in f.readlines()]

    # STAR 1: PRODUCT OF NUMBER OF DIFFERENCES == 1 AND == 3 IN LIST OF ADAPTERS
    print('PART 1')
    lines.sort()
    lines.insert(0, 0)
    lines.append(lines[-1] + 3)
    differences = []

    for i, n in enumerate(lines[:-1]):
        differences.append(lines[i+1] - n)

    n3 = differences.count(3)
    n1 = differences.count(1)

    print(f'Number of 1 * number of 3 = {n1} * {n3} = {n1*n3}')

    print('\n----------------------------------------------\n')

    # STAR 2: NUMBER OF POSSIBLE COMBINATIONS OF ADAPTERS
    print('PART 2')

    groups_of_ones = []
    ones = 0
    total_combinations = 0
    in_group = False

    # An adapter is not necessary if it has a difference of 1 with both
    # the previous and the next adapters.
    for diff in differences:
        if diff == 1:
            ones += 1
            in_group = True
        elif diff == 3:
            groups_of_ones.append(ones-1) if in_group else None
            in_group = False
            ones = 0

    groups_of_ones.append(ones-1) if in_group else None

    # A group of one or two consecutive adapters can be combined in 2**n ways
    # Ex: Combinations of 2 adapters: [(0,0), (0,1), (1,0), (1,1)]
    #   -> No one plugged, only one plugged or both plugged.
    #
    # But a group of three adapters cannot have the combination (0,0,0) because
    # the difference of the previous and next adapter will be > 3.
    powers = map(lambda x: 2**x if x < 3 else 2**x - 1, groups_of_ones)
    total_combinations = reduce(lambda x, y: x*y, powers)

    print(f'Total combinations of adapters = {total_combinations}')



if __name__ == "__main__":
    main(sys.argv[1])
