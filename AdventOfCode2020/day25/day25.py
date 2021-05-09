#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys


def get_key(subject, divisor, loop, value=1):
    for i in range(loop):
        value *= subject
        value %= divisor

    return value

def get_loop_size(pub_key, subject, divisor, value=1):
    loop = 0
    while value != pub_key:
        value *= subject
        value %= divisor
        loop += 1

    return loop


def main(input_file):

    with open(input_file, 'r') as f:
        public_keys = [int(x) for x in f.readlines()]

    subject = 7
    divisor = 20201227
    loop_sizes = [get_loop_size(pub_key, subject, divisor) for pub_key in public_keys]

    encryption_key = get_key(public_keys[0], divisor, loop_sizes[1])

    print(f'Loop sizes: {loop_sizes[0]} {loop_sizes[1]}\n')
    print(f'Encryption key = {encryption_key}')


if __name__ == "__main__":
    main(sys.argv[1])
