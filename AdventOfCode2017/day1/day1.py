#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys


def main(input_file):

    with open(input_file, 'r') as f:
        number = f.read()
 
    number_with_first = number + number[-1]
    total = 0

    for i in range(len(number_with_first)-1):
        if number_with_first[i] == number_with_first[i+1]:
            total += int(number_with_first[i])

    print('PART 1')
    print(f'Total = {total}')

    print('\n----------------------------------------\n')

    number_len = len(number)
    step = number_len // 2
    total = 0

    for i in range(number_len):
        index = (i+step) % number_len
        if number[i] == number[index]:
            total += int(number[i])

    print('PART 2')
    print(f'Total = {total}')


if __name__ == "__main__":
    main(sys.argv[1])
