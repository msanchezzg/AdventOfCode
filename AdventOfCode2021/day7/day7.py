# -*- coding: utf-8 -*-


import argparse
from statistics import median


def cost_movement_1(num_moves):
    return num_moves

def cost_movement_2(num_moves):
    return sum(range(1, num_moves+1))

def get_movement_cost(position, target_pos, cost_func):
    return cost_func(abs(position - target_pos))

def get_total_movement_cost(horizontal_positions, target_pos, cost_func):
    return sum([get_movement_cost(hp, target_pos, cost_func) for hp in horizontal_positions])


def main(input_file):

    with open(input_file, "r") as f:
        horizontal_positions = [int(x) for x in f.read().split(',')]

    # Part 1. The median of the positions is the optimal target position

    pos_min_cost = int(median(horizontal_positions))
    min_cost = sum([abs(hp - pos_min_cost) for hp in horizontal_positions])

    print('PART 1')
    print(f'Position of minimum fuel cost = {pos_min_cost}')
    print(f'Minimum fuel = {min_cost}')

    print('\n----------------------------------------------\n')

    # Part 2. Brute force approach

    min_pos = min(horizontal_positions)
    max_pos = max(horizontal_positions)
    pos_min_cost = -1
    min_cost = -1

    for pos in range(min_pos, max_pos+1):
        cost = get_total_movement_cost(horizontal_positions, pos, cost_movement_2)
        if min_cost == -1 or cost < min_cost:
            min_cost = cost
            pos_min_cost = pos

    print('PART 2')
    print(f'Position of minimum fuel cost = {pos_min_cost}')
    print(f'Minimum fuel = {min_cost}')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Python3 template file for Advent of Code problems"
    )
    parser.add_argument("input_file", type=str, help="File with problem input")

    args = parser.parse_args()
    main(args.input_file)
