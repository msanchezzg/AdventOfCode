#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import knothhash as kh


def main(input_file):

    with open(input_file, 'r') as f:
        lengths_str = f.read().strip()

    lengths_1 = [int(x) for x in lengths_str.split(',')]
    # num_elements = 5    # example case
    num_elements = 256  # input

    # STAR 1
    numbers_1 = kh.knot_hash_loop(num_elements, lengths_1, 1)
    n_0 = numbers_1[0]
    n_1 = numbers_1[1]
    print('PART 1')
    print(f'Final list order: {numbers_1}')
    print(f'\nFirst two numbers multiplied = {n_0} x {n_1} = {n_0 * n_1}')

    print('\n----------------------------------------\n')

    # STAR 2
    hex_str = kh.knot_hash(lengths_str, num_elements=256)

    print('PART 2')
    print(f'\nHex representation = {hex_str}')



if __name__ == "__main__":
    main(sys.argv[1])
