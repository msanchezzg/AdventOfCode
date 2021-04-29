#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
from ast import literal_eval
from dataclasses import dataclass
import re
import operations as op


@dataclass
class Operation:
    opcode: int
    a: int
    b: int
    c: int

    def exe_func(self, func, registers):
        return func(registers, self.a, self.b, self.c)

@dataclass
class CPUSample:
    registers_before: list
    operation: Operation
    registers_after: list


def all_opcodes_1_func(opcodes_operations):
    for _, possible_operations in opcodes_operations.items():
        if len(possible_operations) > 1:
            return False
    return True


def main(input_file):

    with open(input_file, 'r') as f:
        part1, part2 = f.read().split('\n\n\n\n')
    
    sample_format = re.compile(r'Before:\s+(.*)\n(.*)\s+(.*)\s+(.*)\s+(.*)\nAfter:\s+(.*)')

    cpu_samples = []
    possible_operations = {}
    
    for sample in part1.split('\n\n'):
        g = [literal_eval(x) for x in sample_format.match(sample).groups()]
        registers_before, opcode, a, b, c, registers_after = g
        cpu_samples.append(CPUSample(
            registers_before,
            Operation(opcode, a, b, c),
            registers_after
        ))
        possible_operations[opcode] = set()

    part1_opcodes = 0
    for sample in cpu_samples:
        possible_op_counter = 0
        for op_name, op_func in op.all_operations.items():
            end_registers = sample.operation.exe_func(op_func, sample.registers_before)
            
            if end_registers == sample.registers_after:
                possible_operations[sample.operation.opcode].add(op_name)
                possible_op_counter += 1

        if possible_op_counter >= 3:
            part1_opcodes += 1

    print('PART 1')
    print(f'Opcodes with 3 or more function options = {part1_opcodes}')

    print('\n-------------------------------------\n')

    # Assign an operation to each opcode
    while not all_opcodes_1_func(possible_operations):
        for opcode, operations in possible_operations.items():
            if len(operations) == 1:
                f = list(operations)[0]
                for opcode2, operations2 in possible_operations.items():
                    if opcode2 != opcode and f in operations2:
                        operations2.remove(f)
    opcodes_operations = {}
    for opcode, operation in possible_operations.items():
        opcodes_operations[opcode] = list(operation)[0]

    print('PART 2')
    print('Opcodes and functions:')
    for opcode, operation in sorted(opcodes_operations.items()):
        print(f'\t{opcode}: {operation}')
    operations_sequence = []
    for operation in part2.split('\n'):
        opcode, a, b, c = [int(x) for x in operation.split()]
        operations_sequence.append(Operation(opcode, a, b, c))

    # Execute all operations
    registers = [0, 0, 0, 0]
    for operation in operations_sequence:
        func_name = opcodes_operations[operation.opcode]
        func = op.all_operations[func_name]
        registers = operation.exe_func(func, registers)

    print()
    print(f'Final state of registers: {registers}')


if __name__ == "__main__":
    main(sys.argv[1])
