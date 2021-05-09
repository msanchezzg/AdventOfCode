#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys


def get_nth_number(numbers, nth):
    numbers_last_accesses = {}
    i = 0

    for i,n in enumerate(numbers, 1):
        numbers_last_accesses[n] = (0,i)

    i += 1
    next_n = numbers[-1]

    while i <= nth:
        prev_last_acc, last_acc = numbers_last_accesses[next_n]
        if prev_last_acc == 0:
            next_n = 0
        else:
            next_n = last_acc - prev_last_acc

        prev_last_acc, last_acc = numbers_last_accesses.get(next_n,(0,0))
        numbers_last_accesses[next_n] = (last_acc, i)
        i += 1

    return next_n


def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.read()

    numbers = [int(x) for x in lines.split(',')]
    
    print('PART 1')
    index = 2020
    n = get_nth_number(numbers, index)
    print(f'Number spoken in {index} position = {n}')

    print('\n------------------------------------------------\n')

    print('PART 2')
    index = 30000000
    n = get_nth_number(numbers, index)
    print(f'Number spoken in {index} position = {n}')



if __name__ == "__main__":
    main(sys.argv[1])
