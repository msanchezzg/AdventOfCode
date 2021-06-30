#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
from copy import copy
import numpy as np


neighs_increments = (
    ('n', (0, -2)),   ('s', (0, +2)),
    ('nw', (-1, -1)), ('ne', (+1, -1)),
    ('sw', (-1, +1)), ('se', (+1, +1)),
)

def manhattan_distance(cell1, cell2):
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])


def get_cell_index(path, start_cell):
    cell = list(start_cell)
    furthest_cell = start_cell
    furthest_distance = 0
    while path != []:
        move = path.pop(0)
        for coord, increment in neighs_increments:
            if move == coord:
                cell[0] += increment[0]
                cell[1] += increment[1]

            distance = manhattan_distance(start_cell, cell)
            if distance > furthest_distance:
                furthest_cell = copy(cell)
                furthest_distance = distance            

    return tuple(cell), tuple(furthest_cell)


def same_sign(cell1, cell2):
    same_sign_x = (cell1[0] * cell2[0]) >= 0
    same_sign_y = (cell1[1] * cell2[1]) >= 0
    return same_sign_x and same_sign_y



def get_min_moves(initial_cell, final_cell):
    moves = []
    for coord, increment in neighs_increments:
        if same_sign(final_cell, increment):
            moves.append((coord, increment))

    if final_cell == initial_cell:
        moves = moves[-2:]

    # Solving the linear equation system Ax = b,
    # where A is the matrix of coefficients of possible moves
    # and b is the final cell
    A = np.array([list(increment) for _, increment in moves])
    A = np.transpose(A)
    b = np.array(final_cell)
    x = np.linalg.solve(A, b).astype(int)

    simplified_moves = []
    for i, m in enumerate(moves):
        for _ in range(x[i]):
            simplified_moves.append(m[0])

    return simplified_moves


def main(input_file):

    with open(input_file, 'r') as f:
        paths = f.read().split('\n')

    initial_cell = (0, 0)
    for path in paths:
        path = path.split(',')
        # print(path)
        final_cell, furthest_cell = get_cell_index(path, initial_cell)
        simplified_moves1 = get_min_moves(initial_cell, final_cell)
        simplified_moves2 = get_min_moves(initial_cell, furthest_cell)

        print(f'PART 1 - Simplified moves = {len(simplified_moves1)}', end=' ')
        # print(simplified_moves1)
        print()
        print(f'PART 2 - Moves to furthest cell ({furthest_cell}) = {len(simplified_moves2)}', end=' ')
        # print(simplified_moves2)
        print()

if __name__ == "__main__":
    main(sys.argv[1])
