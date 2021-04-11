#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys


def get_cell_value(row, col, serial_number):
    rack_id = row + 10
    power_level = (rack_id * col) + serial_number
    power_level *= rack_id

    if power_level >= 100:
        power_level = int(str(power_level)[-3])
    else:
        power_level = 0

    power_level -= 5
    return power_level

def submatrix_total(matrix, top_row, bottom_row, left_col, right_col):
    total = 0
    for row in range(top_row, bottom_row):
        for col in range(left_col, right_col):
            total += matrix[row][col]

    return total


def main(input_file):

    with open(input_file, 'r') as f:
        serial_number = int(f.read())

    matrix = []
    matrix_size = 300
    for _ in range(matrix_size):
        row = [0]*matrix_size
        matrix.append(row)

    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row][col] = get_cell_value(row+1, col+1, serial_number)


    # { submatrix_size : [((row, col), total_power of 3x3 square with top left cell at (row, col))]}
    submatrices_total_power = {}

    # Since there are a lot of negative powers, total submatrix values start to decrease past size 20,
    # so I try only range [3, 21)
    # Source: u/sciyoshi on Reddit r/adventofcode
    # https://www.reddit.com/r/adventofcode/comments/a53r6i/2018_day_11_solutions/
    for submatrix_size in range(3, 21):
        submatrices_total_power[submatrix_size] = []
        for row in range(matrix_size - submatrix_size):
            for col in range(matrix_size - submatrix_size):
                submatrix_power = submatrix_total(matrix, row, row+submatrix_size, col, col+submatrix_size)
                submatrices_total_power[submatrix_size].append(((row+1, col+1), submatrix_power))

    # Get top left cell with most total power for each square size
    submatrices_max_powers = {}
    for submatrix_size, submatrices_powers in submatrices_total_power.items():
        submatrices_powers.sort(key=lambda x: x[1], reverse=True)
        submatrices_max_powers[submatrix_size] = submatrices_powers[0]

    print('PART 1')
    max_power_top_cell, max_power = submatrices_max_powers[3]
    print(f'Top left cell of square 3x3 with most total power = {max_power_top_cell} (Value = {max_power})')

    print('\n--------------------------------\n')

    max_power_top_cell = (0,0)
    max_power = 0
    max_power_square_size = 0
    for submatrix_size, (cell, power) in submatrices_max_powers.items():
        if power > max_power:
            max_power = power
            max_power_top_cell = cell
            max_power_square_size = submatrix_size

    print('PART 2')
    print(f'Square size with most total power = {max_power_square_size}')
    print(f'Top left cell of square {max_power_square_size}x{max_power_square_size} with most total power = {max_power_top_cell} (Value = {max_power})')



if __name__ == "__main__":
    main(sys.argv[1])
