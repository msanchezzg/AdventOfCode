#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys

from instruction import Instruction


def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    instructions = []
    instructions_visited = set()

    for i, l in enumerate(lines):
        op, arg = l.split(' ')
        arg = int(arg)
        instructions.append(Instruction(op, arg, i))

    while True:
        i = instructions[Instruction.next_instruction]
        if i in instructions_visited:
            print(f'Instruction repeated: {i}')
            print(f'Accumulator: {Instruction.accumulator}')
            break

        i.execute()
        instructions_visited.add(i)



if __name__ == "__main__":
    main(sys.argv[1])
