#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import re


def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().split('\n\n')

    valid_passports = 0

    fields = [
        r'(byr:(19[2-9][0-9]|200[0-2]))(\s|$)',         # Birth year
        r'(iyr:20(1[0-9]|20))(\s|$)',                   # Issue year
        r'(eyr:20(2[0-9]|30))(\s|$)',                   # Expiration year
        r'(hgt:(((1[5-8][0-9]|19[0-3])cm)|(59|6[0-9]|7[0-6])in))(\s|$)',    # Height
        r'(hcl:#([0-9]|[a-f]){6})(\s|$)',               # Hair color
        r'(ecl:(amb|blu|brn|gry|grn|hzl|oth))(\s|$)',   # Eye color
        r'(pid:([0-9]){9})(\s|$)'                       # PID
    ]

    regex_fields = [re.compile(f) for f in fields]

    for passport in lines:
        if all([f.search(passport) for f in regex_fields]):
            valid_passports += 1

    print(f'Valid passports: {valid_passports}')


if __name__ == "__main__":
    main(sys.argv[1])
