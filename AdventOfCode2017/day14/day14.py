#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import knothhash as kh


class Point:
    def __init__(self, x=0, y=0, group_id=-1):
        self.x = x
        self.y = y
        self.group_id = group_id

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.group_id})'

    def __hash__(self):
        return hash((self.x, self.y, self.group_id))

    def equal_coords(self, other):
        if not isinstance(other, Point):
            return False

        return self.x == other.x and self.y == other.y

    def is_neighbor(self, other):
        if not isinstance(other, Point):
            return False

        return (self.x == other.x and self.y - other.y in (-1,0,1))  or \
                (self.y == other.y and self.x - other.x in (-1,0,1))

    def get_neighbors_from_candidates(self, candidates, include_self=True):
        filter_func = self.is_neighbor if include_self else \
            lambda p: self.is_neighbor(p) and not self.equal_coords(p)

        return list(filter(filter_func, candidates))


USED = '1'
NON_USED = '0'


def get_points_used(matrix):
    points = []
    for x, row in enumerate(matrix):
        for y, square in enumerate(row):
            if square == USED:
                points.append(Point(x, y))
    return points


def main(input_file):

    with open(input_file, 'r') as f:
        key_str = f.read().strip()

    nrows = 128
    hashes = [kh.knot_hash(f'{key_str}-{i}') for i in range(nrows)]
    binary_hashes = [f'{int(h, 16):0>128b}' for h in hashes]

    print('PART 1')
    num_ones = sum([bin.count(USED) for bin in binary_hashes])
    print(f'Number of used squares = {num_ones}')

    print('\n----------------------------------------\n')

    matrix = [list(h) for h in binary_hashes]
    groups = []
    used_squares = get_points_used(matrix)
    next_group_id = 0

    for used_sq in used_squares:
        if used_sq.group_id == -1:
            used_sq.group_id = next_group_id
            groups.append([used_sq])
            next_group_id += 1

        neighbors = used_sq.get_neighbors_from_candidates(used_squares, include_self=False)
        for neigh in neighbors:
            if neigh.group_id == -1:
                neigh.group_id = used_sq.group_id
                groups[used_sq.group_id].append(neigh)
            elif neigh.group_id != used_sq.group_id:
                min_group_id = min(neigh.group_id, used_sq.group_id)
                max_group_id = max(neigh.group_id, used_sq.group_id)

                # move squares from max_group to min_group
                for sq in groups[max_group_id]:
                    sq.group_id = min_group_id
                    groups[min_group_id].append(sq)
                groups[max_group_id] = []

    groups_not_empty = [g for g in groups if g != []]

    print('PART 2')
    print(f'Number of groups = {len(groups_not_empty)}')



if __name__ == "__main__":
    main(sys.argv[1])
