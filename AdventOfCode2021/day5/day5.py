# -*- coding: utf-8 -*-


import argparse
from collections import Counter


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def get_points_in_line_1(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        if dx != 0:
            sign_dx = dx//abs(dx)
        if dy != 0:
            sign_dy = dy//abs(dy)
        points = []

        if dx == 0:     # Vertical line
            for d in range(0,dy+sign_dy,sign_dy):
                points.append(Point(self.x, self.y-d))
        elif dy == 0:   # Horizontal line
            for d in range(0,dx+sign_dx,sign_dx):
                points.append(Point(self.x-d, self.y))

        return points

    def get_points_in_line_2(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        if dx != 0:
            sign_dx = dx//abs(dx)
        if dy != 0:
            sign_dy = dy//abs(dy)

        points = []

        if dx == 0:     # Vertical line
            for d in range(0,dy+sign_dy,sign_dy):
                points.append(Point(self.x, self.y-d))
        elif dy == 0:   # Horizontal line
            for d in range(0,dx+sign_dx,sign_dx):
                points.append(Point(self.x-d, self.y))
        elif abs(dx) == abs(dy):    # Diagonal line
            for x in range(0,dx+sign_dx,sign_dx):
                for y in range(0,dy+sign_dy,sign_dy):
                    if abs(x) != abs(y):
                        continue
                    points.append(Point(self.x-x, self.y-y))

        return points


def main(input_file):

    with open(input_file, "r") as f:
        lines = f.read().split('\n')

    points_1 = []
    points_2 = []
    for line in lines:
        x1, y1, x2, y2 = [int(x) for x in line.replace(' -> ', ',').split(',')]
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        points_1 += p1.get_points_in_line_1(p2)
        points_2 += p1.get_points_in_line_2(p2)

    counter_1 = Counter(points_1)
    counter_2 = Counter(points_2)
    num_points_repeated_1 = sum(1 for point, times in counter_1.items() if times >= 2)
    num_points_repeated_2 = sum(1 for point, times in counter_2.items() if times >= 2)

    print('PART 1')
    print(f'Number of points repeated = {num_points_repeated_1}')

    print('\n-----------------------------\n')

    print('PART 2')
    print(f'Number of points repeated = {num_points_repeated_2}')



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Python3 template file for Advent of Code problems"
    )
    parser.add_argument("input_file", type=str, help="File with problem input")

    args = parser.parse_args()
    main(args.input_file)
