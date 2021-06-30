#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys


class Layer:
    def __init__(self, id, depth):
        self.id = id
        self.depth = depth

    def __repr__(self):
        return str(self.__dict__)

    def get_laser_position_by_time(self, picosecond):
        # Hint from Reddit
        # https://www.reddit.com/r/adventofcode/comments/7jgyrt/2017_day_13_solutions/
        position = picosecond % ((self.depth-1) * 2)
        return position


def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.readlines()

    layers = []
    for line in lines:
        layer_id, layer_depth = [int(x) for x in line.split(': ')]
        layers.append(Layer(layer_id, layer_depth))

    print('PART 1')
    severity = 0
    for lay in layers:
        picosecond = lay.id
        pos = lay.get_laser_position_by_time(picosecond)
        if pos == 0:
            print(f'Collision in layer {lay}')
            severity += (lay.id * lay.depth)

    print(f'\nSeverity = {severity}')

    print('\n-----------------------------------\n')
    print('PART 2')

    delay = 0
    collision = True
    while collision:
        collision = False
        delay += 1
        # print(delay, file=sys.stderr)
        for lay in layers:
            picosecond = lay.id + delay
            pos = lay.get_laser_position_by_time(picosecond)
            if pos == 0:
                collision = True
                break

    print(f'Min delay without collisions = {delay}')


if __name__ == "__main__":
    main(sys.argv[1])
