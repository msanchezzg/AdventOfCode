#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys


def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().split('\n\n')

    valid_passports = 0

    fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']   # 'cid:' is not mandatory

    for passport in lines:
        if all([f in passport for f in fields]):
            valid_passports += 1

    print(f'Valid passports: {valid_passports}')


if __name__ == "__main__":
    main(sys.argv[1])
