#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys


def main(input_file):

    with open(input_file, 'r') as f:
        lines = [l for l in f.read().split('\n') if l]

    trees_counter = 0
    period_len = len(lines[0])

    for i, line in enumerate(lines[1:], 1):
        pos = (3*i) % period_len
        if line[pos] == '#':
            trees_counter += 1

    print(f'Number of trees = {trees_counter}')


if __name__ == "__main__":
    main(sys.argv[1])
