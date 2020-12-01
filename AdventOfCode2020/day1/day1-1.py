#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys


def main(input_file):

    with open(input_file, 'r') as f:
        numbers = [int(x) for x in f.readlines()]

    found = False
    for i, n in enumerate(numbers):
        if found:
            break
        for _, m in enumerate(numbers[i+1:]):
            if n+m == 2020:
                print(f'numbers are: {n}, {m}\nProduct = {n*m}')
                found = True
                break


if __name__ == "__main__":
    main(sys.argv[1])
