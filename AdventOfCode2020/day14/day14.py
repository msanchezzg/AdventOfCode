#!/usr/bin/python3
#-*- coding: utf-8 -*-

import itertools
import sys
import re


def get_bin_value(int_value, bits=36):
    bin_value = bin(int_value)[2:]
    return format(int(bin_value), f'0{bits}')

def get_real_value(value, mask):
    real_value_bin = apply_mask_star1(value, mask)
    return int(real_value_bin, 2)

def apply_mask_star1(value, mask):
    bin_value = list(get_bin_value(value))
    for i, b in enumerate(mask):
        if b != 'X':
            bin_value[i] = b

    bin_value = ''.join(bin_value)
    return bin_value

def apply_mask_star2(value, mask):
    bin_value = list(get_bin_value(value))
    for i, b in enumerate(mask):
        if b != '0':
            bin_value[i] = b

    bin_value = ''.join(bin_value)
    return bin_value

def get_possible_values(value, mask):
    possible_values = []
    bin_value = apply_mask_star2(value, mask)
    floating_bits = bin_value.count('X')
    floating_bits_pos = [i for i,b in enumerate(bin_value) if b == 'X']
    combinations_0_1 = list(itertools.product([0, 1], repeat=floating_bits))

    for comb in combinations_0_1:
        replacements = zip(comb, floating_bits_pos)
        new_bin_value = list(bin_value)
        for bit, pos in replacements:
            new_bin_value[pos] = str(bit)

        new_bin_value = ''.join(new_bin_value)
        possible_values.append(int(new_bin_value, 2))

    return possible_values


def star1(lines):
    mask_line_format = r'^mask = ([X,0,1]{36})$'
    mem_line_format = r'^mem\[(\d*)\] = (\d*)$'

    memory = dict()
    mask = 0

    print('PART 1')
    for line in lines:
        if re.match(mask_line_format, line):
            mask = re.match(mask_line_format, line).groups()[0]
        else:
            mem_pos, value = [int(x) for x in re.match(mem_line_format, line).groups()]
            real_value = get_real_value(value, mask)
            memory[mem_pos] = real_value

    total = 0
    for mem_pos, value in memory.items():
        total += value

    print(f'Sum of values in memory = {total}')

def star2(lines):
    mask_line_format = r'^mask = ([X,0,1]{36})$'
    mem_line_format = r'^mem\[(\d*)\] = (\d*)$'

    memory = dict()
    mask = 0

    print('PART 2')

    for line in lines:
        if re.match(mask_line_format, line):
            mask = re.match(mask_line_format, line).groups()[0]
        else:
            mem_pos, value = [int(x) for x in re.match(mem_line_format, line).groups()]

            all_mem_pos = get_possible_values(mem_pos, mask)
            for mem_pos in all_mem_pos:
                memory[mem_pos] = value

    total = 0
    for mem_pos, value in memory.items():
        total += value

    print(f'Sum of values in memory = {total}')


def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().split('\n')

    star1(lines)
    print('\n-------------------------------------------------\n')
    star2(lines)


if __name__ == "__main__":
    main(sys.argv[1])