#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys


def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.read().split('\n')
    
    spreadsheet = [[int(x) for x in row.split()] for row in lines]
    checksum = 0
    for row in spreadsheet:
        max_n = max(row)
        min_n = min(row)
        checksum += max_n - min_n

    print('PART 1')
    print(f'Checksum = {checksum}')

    print('\n----------------------------------------\n')

    checksum = 0
    for row in spreadsheet:
        sorted_row = sorted(row, reverse=True)
        found_divisors = False
        for i, n in enumerate(sorted_row):
            if found_divisors:
                break
            for i2, n2 in enumerate(sorted_row[i+1:]):
                if n2 != 0 and n % n2 == 0:
                    checksum += n // n2
                    found_divisors = True
                    break
    print('PART 2')
    print(f'Checksum = {checksum}')

if __name__ == "__main__":
    main(sys.argv[1])
