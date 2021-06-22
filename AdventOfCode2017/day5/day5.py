#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
from copy import copy


def main(input_file):

    with open(input_file, 'r') as f:
        instructions_star2 = [int(x) for x in f.readlines()]

    instructions_star1 = copy(instructions_star2)
    instruction_index = 0
    steps = 0
    while instruction_index < len(instructions_star1):
        inst = instructions_star1[instruction_index]
        instructions_star1[instruction_index] += 1
        instruction_index += inst
        steps += 1

    print('PART 1')
    print(f'Steps before exit = {steps}')

    print('\n--------------------------------------\n')
    
    instruction_index = 0
    steps = 0
    while instruction_index < len(instructions_star2):
        inst = instructions_star2[instruction_index]
        instructions_star2[instruction_index] = inst + 1 if inst < 3 else inst - 1
        instruction_index += inst
        steps += 1

    print('PART 2')
    print(f'Steps before exit = {steps}')


if __name__ == "__main__":
    main(sys.argv[1])
