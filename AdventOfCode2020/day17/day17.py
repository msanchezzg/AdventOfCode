#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from copy import deepcopy
from point import PointState, Point4D


def get_extremes4D(active_points):
    min_active_x = min([p.x for p in active_points])
    max_active_x = max([p.x for p in active_points])
    min_active_y = min([p.y for p in active_points])
    max_active_y = max([p.y for p in active_points])
    min_active_z = min([p.z for p in active_points])
    max_active_z = max([p.z for p in active_points])
    min_active_w = min([p.w for p in active_points])
    max_active_w = max([p.w for p in active_points])

    return [min_active_x, max_active_x, min_active_y, max_active_y,
        min_active_z, max_active_z, min_active_w, max_active_w]


def star1(active_points, iterations):

    active_points_copy = set()
    min_active_x, max_active_x, \
    min_active_y, max_active_y, \
    min_active_z, max_active_z, _, _ = get_extremes4D(active_points)

    for i in range(iterations):
        active_points_copy = deepcopy(active_points)
        for x in range(min_active_x-1, max_active_x+2):
            for y in range(min_active_y-1, max_active_y+2):
                for z in range(min_active_z-1, max_active_z+2):
                    point = Point4D(x,y,z)
                    neighbors = point.get_neighbors()
                    active_neighbors = len([n for n in neighbors if n in active_points_copy])

                    if point in active_points_copy:
                        if active_neighbors != 2 and active_neighbors != 3:                            
                            active_points.remove(point)
                    else:
                        if active_neighbors == 3:
                            active_points.add(point)

        min_active_x, max_active_x, \
        min_active_y, max_active_y, \
        min_active_z, max_active_z, _, _ = get_extremes4D(active_points)
        print(f'Active points after iteration {i+1} = {len(active_points)}')


def star2(active_points, iterations):

    active_points_copy = set()
    min_active_x, max_active_x, \
    min_active_y, max_active_y, \
    min_active_z, max_active_z, \
    min_active_w, max_active_w = get_extremes4D(active_points)

    for i in range(iterations):
        active_points_copy = deepcopy(active_points)
        for x in range(min_active_x-1, max_active_x+2):
            for y in range(min_active_y-1, max_active_y+2):
                for z in range(min_active_z-1, max_active_z+2):
                    for w in range(min_active_w-1, max_active_w+2):
                        point = Point4D(x, y, z, w)
                        neighbors = point.get_neighbors()
                        active_neighbors = len([n for n in neighbors if n in active_points_copy])

                        if point in active_points_copy:
                            if active_neighbors != 2 and active_neighbors != 3:                            
                                active_points.remove(point)
                        else:
                            if active_neighbors == 3:
                                active_points.add(point)

        min_active_x, max_active_x, \
        min_active_y, max_active_y, \
        min_active_z, max_active_z, \
        min_active_w, max_active_w = get_extremes4D(active_points)
        print(f'Active points after iteration {i+1} = {len(active_points)}')



def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().split('\n')

    active_points1 = set()
    active_points2 = set()
    for x, line in enumerate(lines):
        for y, cell in enumerate(line):
            cell_state = None
            for state in PointState:
                if cell == state.value:
                    cell_state = state

            point = Point4D(x, y, 0, 0)
            if cell_state == PointState.ACTIVE:
                active_points1.add(point)
                active_points2.add(point)

    print('PART 1')
    star1(active_points1, iterations=6)

    print('\n---------------------------------------------------------\n')

    print('PART 2')
    star2(active_points2, iterations=6)


if __name__ == "__main__":
    main(sys.argv[1])
