#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
from matrix import Matrix


def main(input_file):

    with open(input_file, 'r') as f:
        data = [list(line) for line in f.read().split('\n')]

    matrix = Matrix(data)
    history = set()
    minute = 0
    while True:
        imm = matrix.immutable()
        if imm in history:
            break
        history.add(imm)
        matrix = matrix.evolve()
        minute += 1

    print('PART 1')
    print(f'State repeated in minute {minute}')
    matrix.pretty_print()
    biodiversity = matrix.get_total_biodiversity()
    print(f'Matrix biodiversity = {biodiversity}')


if __name__ == "__main__":
    main(sys.argv[1])
