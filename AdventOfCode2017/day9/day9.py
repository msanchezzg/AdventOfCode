#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys


def get_total_groups_value(line):
    group_level = 0
    total_value = 0
    chars_in_garbage = 0
    in_garbage = False
    ignore_next = False

    for character in line:
        if ignore_next:
            ignore_next = False
            continue

        if not in_garbage:
            if character == '<':
                in_garbage = True
            elif character == '{':
                group_level += 1
            elif character == '}':
                total_value += group_level
                group_level -= 1
        else:
            if character == '>':
                in_garbage = False
            elif character == '!':
                ignore_next = True
            else:
                chars_in_garbage += 1

    return total_value, chars_in_garbage


def main(input_file):

    with open(input_file, 'r') as f:
        line = f.read()

    total_value, chars_in_garbage = get_total_groups_value(line)
    print(f'PART 1 - Total value of groups = {total_value}')
    print(f'PART 2 - Characters inside garbage = {chars_in_garbage}')


if __name__ == "__main__":
    main(sys.argv[1])
