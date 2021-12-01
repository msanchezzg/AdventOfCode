# -*- coding: utf-8 -*-


import argparse


def count_increments(listt):
    num_increments = 0
    for i in range(1, len(listt)):
        if listt[i] > listt[i-1]:
            num_increments += 1

    return num_increments


def main(input_file):

    with open(input_file, "r") as f:
        numbers = [int(x) for x in f.read().split('\n')]

    print('PART 1')
    print(f'Number of increments = {count_increments(numbers)}')

    print('\n-----------------------------\n')

    numbers_group_3 = [numbers[i]+numbers[i+1]+numbers[i+2] for i in range(len(numbers)-2)]
    print('PART 2')
    print(f'Number of increments = {count_increments(numbers_group_3)}')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Python3 template file for Advent of Code problems"
    )
    parser.add_argument("input_file", type=str, help="File with problem input")

    args = parser.parse_args()
    main(args.input_file)
