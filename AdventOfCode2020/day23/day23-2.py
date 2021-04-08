#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from linkedlist import Node


def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.read()

    cups = [int(x) for x in list(lines)]
    # top_cup = 9           # Part 1
    top_cup = 1000000
    max_cup = top_cup
    for i in range(max_cup+1, top_cup+1):
        cups.append(i)

    nodes_by_value = {}

    for c in cups:
        nodes_by_value[c] = Node(c)
    for i, c in enumerate(cups):
        if i-1 >= 0:
            prev_cup_value = cups[i-1]
        else:
            prev_cup_value = cups[top_cup-1]

        if i+1 < top_cup:
            next_cup_value = cups[i+1]
        else:
            next_cup_value = cups[0]

        node = nodes_by_value[c]
        node.prev = nodes_by_value[prev_cup_value]
        node.next = nodes_by_value[next_cup_value]


    moves = 10000000
    # moves = 100       # Part 1
    current_cup = nodes_by_value[cups[0]]

    for move in range(moves):
        # print(move)
        cups_picked = [current_cup.pop_next() for _ in range(3)]

        cups_picked_values = [c.value for c in cups_picked]

        i = 1
        while True:
            dest_cup_value = current_cup.value - i

            if dest_cup_value <= 0:
                # max_cup = max(cups)
                max_cup = top_cup
                while max_cup in cups_picked_values:
                    max_cup -= 1
                dest_cup = nodes_by_value[max_cup]
                break

            if dest_cup_value not in cups_picked_values:
                dest_cup = nodes_by_value[dest_cup_value]
                break
            i += 1

        n = dest_cup
        for cp in cups_picked:
            n.add_next_node(cp)
            n = cp

        current_cup = current_cup.next

    cup1 = nodes_by_value[1]

    ## Part 1
    # nextt = cup1.next
    # order = ''
    # while nextt.value != 1:
    #     order += str(nextt.value)
    #     nextt = nextt.next

    # print(f'Order = {order}')

    next1 = cup1.next.value
    next2 = cup1.next.next.value
    print('PART 2')
    print(f'Product of 2 cups next to cup 1 = {next1} * {next2} = {next1*next2}')


if __name__ == "__main__":
    main(sys.argv[1])
