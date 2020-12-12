#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import re

from ships import Ship, MovingShip
from directions import Instruction


def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    instruction_re = r'([N,S,W,E,L,R,F]{1})(\d*)\s*'
    instructions = []
    for line in lines:
        matches = re.match(instruction_re, line).groups()
        direction, n = matches
        instructions.append(Instruction(direction, int(n)))

    # STAR 1
    print('PART 1')
    ship = Ship()
    for instruction in instructions:
        ship.move(instruction)

    manhattan_dist = abs(ship.hor_axis) + abs(ship.vert_axis)
    print(f'Ship\'s final state: {ship}')
    print(f"Ship's Manhattan distance = {manhattan_dist}")

    print('\n-------------------------------------------------------\n')

    # STAR 2: MOVE SHIP REFERENT TO A WAYPOINT
    print('PART 2')
    ship = MovingShip()
    for instruction in instructions:
        ship.move(instruction)


    manhattan_dist = abs(ship.hor_axis) + abs(ship.vert_axis)
    print(f'Ship\'s final state: {ship}')
    print(f'Waypoint\'s final state: {ship.waypoint}')
    print(f"Ship's Manhattan distance = {manhattan_dist}")


if __name__ == "__main__":
    main(sys.argv[1])
