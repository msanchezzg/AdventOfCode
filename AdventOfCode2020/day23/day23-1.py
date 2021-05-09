#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys


def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.read()

    cups = [int(x) for x in list(lines)]
    num_cups = len(cups)
    moves = 100
    current_cup = (0, cups[0])      # (Index, value)

    for _ in range(moves):
        cups_picked = [
            (cups[(current_cup[0]+1) % num_cups]),
            (cups[(current_cup[0]+2) % num_cups]),
            (cups[(current_cup[0]+3) % num_cups]),
        ]

        for i in range(3):
            cups.remove(cups_picked[i])

        i = 1
        dest_cup = (-1, -1)
        while True:
            dest_cup_value = current_cup[1] - i

            if dest_cup_value in cups and dest_cup_value not in cups_picked:
                dest_cup_index = cups.index(dest_cup_value)
                dest_cup = (dest_cup_index, dest_cup_value)
                break
            i += 1
            if i > num_cups:
                max_cup = (cups.index(max(cups)), max(cups))
                dest_cup = max_cup
                break

        for i in range(1, 4):
            cups.insert(dest_cup[0] + i, cups_picked[i-1])

        current_cup_index = (cups.index(current_cup[1]) + 1) % num_cups
        current_cup = (current_cup_index, cups[current_cup_index])

    print('PART 1')
    print(f'Final cups: {cups}')
    index1 = cups.index(1)
    order = ''
    j = 0
    for i in range(num_cups-1):
        j += 1
        cup = cups[(index1 + j) % num_cups]
        order += str(cup)

    print(f'Order = {order}')


if __name__ == "__main__":
    main(sys.argv[1])
