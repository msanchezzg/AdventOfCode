#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys

from plane_seats import PlaneSeats, FLOOR


def main(input_file):
    with open(input_file, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    matrix_border = [[FLOOR] + list(line) + [FLOOR] for line in lines]
    border_row = [FLOOR] * (len(matrix_border[0]))
    matrix_border = [border_row] + matrix_border + [border_row]
    matrix = PlaneSeats(matrix_border)
    matrix_copy = PlaneSeats(matrix_border)

    print('PART 2')
    
    iterations = 0
    while True:
        # Update state
        iterations += 1
        for i in range(1, len(matrix.matrix) - 1):
            for j in range(1, len(matrix.matrix[0]) - 1):
                matrix.matrix[i][j] = matrix_copy.get_cell_next_state_star2(i, j)

        if matrix == matrix_copy:
            break

        # Swap matrices
        matrix_aux = matrix
        matrix = matrix_copy
        matrix_copy = matrix_aux

    print(f'Iteration that repeats a state = {iterations}')
    print(f'Occupied seats: {matrix.get_occupied_seats()}')
    print(f'Empty seats: {matrix.get_empty_seats()}, floor seats: {matrix.get_floor_seats()}')


if __name__ == "__main__":
    main(sys.argv[1])
