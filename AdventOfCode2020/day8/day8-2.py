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

    nops_and_jmps = [i for i in instructions if i.op == 'jmp' or i.op == 'nop']

    last_inst_reached = False

    for change in nops_and_jmps:
        instructions[change.index].change_operation()
        Instruction.reset_state()
        instructions_visited.clear()

        while True:
            next_inst = Instruction.next_instruction
            if next_inst == len(instructions):
                print(f'Accumulator: {Instruction.accumulator}')
                last_inst_reached = True
                break

            i = instructions[next_inst]
            if i in instructions_visited:
                break

            i.execute()
            instructions_visited.add(i)

        if last_inst_reached:
            print(f'Change: {change}', end=' ')
            instructions[change.index].change_operation()
            print(f' <= from {instructions[change.index]}')
            break

        instructions[change.index].change_operation()



if __name__ == "__main__":
    main(sys.argv[1])
