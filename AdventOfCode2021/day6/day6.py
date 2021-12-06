# -*- coding: utf-8 -*-


import argparse
from collections import Counter
from dataclasses import dataclass


@dataclass
class LanternFish:
    creation_day: int
    start_value: int = 8

    def __hash__(self):
        return hash((self.creation_day, self.start_value))


lanternfish_children = {}

def get_num_children(lanternfish: LanternFish, days: int):
    if lanternfish in lanternfish_children:
        return lanternfish_children[lanternfish]

    num_children = 1
    first_child_creation_day = lanternfish.creation_day + 1 + lanternfish.start_value
    rest_days = days - first_child_creation_day
    rest_children = rest_days // 7
    for i in range(rest_children+1):
        creation_day = first_child_creation_day + i*7
        num_children += get_num_children(LanternFish(creation_day), days)

    lanternfish_children[lanternfish] = num_children
    return num_children



def main(input_file):

    with open(input_file, "r") as f:
        lanternfish_start_values = [int(x) for x in f.read().split(',')]

    days_1 = 80
    days_2 = 256
    lanternfish_start_values_counter = Counter(lanternfish_start_values)

    num_lanternfish = 0
    for start_value, times in lanternfish_start_values_counter.items():
        lanternfish = LanternFish(start_value, 0)
        num_children = get_num_children(lanternfish, days_1)
        num_lanternfish += num_children * times

    print('PART 1')
    print(f'Lanternfish after {days_1} days = {num_lanternfish}')

    print('\n----------------------------------------------\n')

    lanternfish_children.clear()
    num_lanternfish = 0

    for start_value, times in lanternfish_start_values_counter.items():
        lanternfish = LanternFish(start_value, 0)
        num_children = get_num_children(lanternfish, days_2)
        num_lanternfish += num_children * times

    print('PART 2')
    print(f'Lanternfish after {days_2} days = {num_lanternfish}')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Python3 template file for Advent of Code problems"
    )
    parser.add_argument("input_file", type=str, help="File with problem input")

    args = parser.parse_args()
    main(args.input_file)
