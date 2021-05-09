#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys


def is_valid(pwd, letter, index1, index2):
    if (pwd[index1] == letter) ^ (pwd[index2] == letter):
        return True
    return False


def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.readlines()

    valid_pwds = 0
    for l in lines:
        counter, letter, pwd = l.split(' ')
        index1, index2 = [int(x)-1 for x in counter.split('-')]
        letter = letter[:-1]
        if is_valid(pwd, letter, index1, index2):
            valid_pwds += 1

    print(f'Valid passwords: {valid_pwds}')



if __name__ == "__main__":
    main(sys.argv[1])
