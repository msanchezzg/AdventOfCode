#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys


def get_num_of_trees(trees_map, right, down, period_len):
    if down != 1:
        return get_num_of_trees(trees_map[::down], right, 1, period_len)

    trees_map2 = trees_map[1:]
    trees_counter = 0

    for i, line in enumerate(trees_map2, 1):
        pos = (right*i) % period_len
        if line[pos] == '#':
            trees_counter += 1

    return trees_counter



def main(input_file):

    with open(input_file, 'r') as f:
        lines = [l for l in f.read().split('\n') if l]

    period_len = len(lines[0])
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    total = 1

    for right, down in slopes:
        trees = get_num_of_trees(lines, right, down, period_len)
        total *= trees
        print(f'Right: {right}, down: {down}. Num of trees = {trees}')

    print(f'\nTotal Number of trees = {total}')


if __name__ == "__main__":
    main(sys.argv[1])
