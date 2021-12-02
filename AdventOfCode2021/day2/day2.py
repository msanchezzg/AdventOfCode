# -*- coding: utf-8 -*-


import argparse
from submarine import Instruction, Submarine, Submarine2


def main(input_file):

    instructions = []
    with open(input_file, "r") as f:
        for line in f.read().split('\n'):
            i, n = line.split()
            instructions.append(Instruction(i, int(n)))

    submarine = Submarine()
    for inst in instructions:
        submarine.move(inst)

    print('PART 1')
    print(f'Horizontal value: {submarine.x}, Depth: {-submarine.y}')
    print(f'Product = {submarine.x * -submarine.y}')

    print('\n-----------------------------\n')

    submarine2 = Submarine2()
    for inst in instructions:
        submarine2.move(inst)

    print('PART 2')
    print(f'Horizontal value: {submarine2.x}, Depth: {submarine2.y}')
    print(f'Product = {submarine2.x * submarine2.y}')



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Python3 template file for Advent of Code problems"
    )
    parser.add_argument("input_file", type=str, help="File with problem input")

    args = parser.parse_args()
    main(args.input_file)
