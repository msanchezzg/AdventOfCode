#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys

def is_valid_star1(passphrase):
    words = passphrase.split()
    return len(words) == len(set(words))


def is_valid_star2(passphrase):
    words = [''.join(sorted(w)) for w in passphrase.split()]
    return len(words) == len(set(words))

def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.read().split('\n')

    valid_passphrases = 0
    for passphrase in lines:
        if is_valid_star1(passphrase):
            valid_passphrases += 1

    print('PART 1')
    print(f'Valid passphrases = {valid_passphrases}')

    print('\n--------------------------------------\n')

    valid_passphrases = 0
    for passphrase in lines:
        if is_valid_star2(passphrase):
            valid_passphrases += 1

    print('PART 2')
    print(f'Valid passphrases = {valid_passphrases}')


if __name__ == "__main__":
    main(sys.argv[1])
