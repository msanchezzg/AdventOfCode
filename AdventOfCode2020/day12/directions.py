#!/usr/bin/python3

from enum import Enum


class Direction(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'
    RIGHT = 'R'
    LEFT = 'L'
    FORWARD = 'F'


class Instruction():

    def __init__(self, direction, n, from_enum=False):
        if not from_enum:
            for d in Direction:
                if direction == d.value:
                    self.direction = d
                    break
        else:
            self.direction = direction

        self.n = n

    def __repr__(self):
        return f'[{self.direction.value} {self.n}]'
