# -*- coding: utf-8 -*-


import argparse
from collections import OrderedDict
from dataclasses import dataclass


@dataclass
class Entry:
    patterns: list()
    outputs: list


def filter_pattern_length(patterns, length):
    return list(filter(lambda pattern: len(pattern) == length, patterns))

def contains_subpatterns(pattern, subpatterns):
    for subp in subpatterns:
        if not subp in pattern:
            return False
    return True

def sort_str(string):
    return ''.join(sorted(string))

def get_pattern_number_correspondence(patterns):
    numbers_by_pattern = {'abcdefg': 8}

    ## Length 2. Number 1
    pattern_1 = filter_pattern_length(patterns, 2)[0]
    numbers_by_pattern[sort_str(pattern_1)] = 1
    top_right_bottom_right_segment = set(list(pattern_1))

    ## Length 3. Number 7
    pattern_7 = filter_pattern_length(patterns, 3)[0]
    numbers_by_pattern[sort_str(pattern_7)] = 7

    ## Length 4. Number 4
    pattern_4 = filter_pattern_length(patterns, 4)[0]
    numbers_by_pattern[sort_str(pattern_4)] = 4
    rest_letters = set(list(pattern_4)) - top_right_bottom_right_segment
    top_left_middle_segment = rest_letters

    ## Length 6. Numbers 0, 6, 9
    patterns_0_6_9 = filter_pattern_length(patterns, 6)
    for pattern in patterns_0_6_9:
        # 0 and 9 must match both the top_right_bottom_right letter possibilities,
        # one for the top_right segment and the other for the bottom_right
        if contains_subpatterns(pattern, top_right_bottom_right_segment):
            # 9 must match both the top_left and the middle segment letter possibilities
            if contains_subpatterns(pattern, top_left_middle_segment):
                numbers_by_pattern[sort_str(pattern)] = 9
            else:
                numbers_by_pattern[sort_str(pattern)] = 0
        # 6 must only match one of the top_right_bottom_right letter possibilities
        # (it does not display the top_right segment)
        else:
            numbers_by_pattern[sort_str(pattern)] = 6

    # Length 5. Numbers 2, 3, 5
    patterns_2_3_5 = filter_pattern_length(patterns, 5)
    for pattern in patterns_2_3_5:
        # 3 must match both the top_right_bottom_right letter possibilities
        if contains_subpatterns(pattern, top_right_bottom_right_segment):
            numbers_by_pattern[sort_str(pattern)] = 3
        else:
            # 5 must match both the top_left and the middle segment letter possibilities
            if contains_subpatterns(pattern, top_left_middle_segment):
                numbers_by_pattern[sort_str(pattern)] = 5
            else:
                numbers_by_pattern[sort_str(pattern)] = 2

    return numbers_by_pattern


def main(input_file):

    with open(input_file, "r") as f:
        lines = f.read().split('\n')

    entries = []
    num_1_4_7_8 = 0
    for line in lines:
        patterns, output = line.split(' | ')
        entry = Entry(patterns.split(), output.split())
        entries.append(entry)

        for output in entry.outputs:
            if len(output) in (2, 3, 4, 7):
                num_1_4_7_8 += 1

    print('PART 1')
    print(f'Number of outputs with number 1, 4, 7 or 8 = {num_1_4_7_8}')

    print('\n----------------------------------------------\n')

    print('PART 2')
    print('Pattern-sum correspondences:')
    signal_sum = 0
    for entry in entries:
        signal = ''
        numbers_by_pattern = get_pattern_number_correspondence(entry.patterns)
        numbers_by_pattern_sorted = sorted(numbers_by_pattern.items(), key=lambda item: item[1])

        for output in entry.outputs:
            signal += str(numbers_by_pattern[sort_str(output)])

        print(f'\t{numbers_by_pattern_sorted}\tSignal: {signal}')

        signal_sum += int(signal)
    
    print(f'\nSum of signals = {signal_sum}')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Python3 template file for Advent of Code problems"
    )
    parser.add_argument("input_file", type=str, help="File with problem input")

    args = parser.parse_args()
    main(args.input_file)
