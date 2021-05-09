#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys


def is_valid(pwd, letter, min_counter, max_counter):
    c = pwd.count(letter)
    if c < min_counter:
        return False
    if c > max_counter:
        return False
    return True


def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.readlines()

    valid_pwds = 0
    for l in lines:
        counter, letter, pwd = l.split(' ')
        min_counter, max_counter = [int(x) for x in counter.split('-')]
        letter = letter[:-1]
        if is_valid(pwd, letter, min_counter, max_counter):
            valid_pwds += 1

    print(f'Valid passwords: {valid_pwds}')



if __name__ == "__main__":
    main(sys.argv[1])
