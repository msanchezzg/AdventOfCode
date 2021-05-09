#!/usr/bin/python3
#-*- coding: utf-8 -*-

import copy


FLOOR = '.'
OCCUPIED = '#'
EMPTY = 'L'

class PlaneSeats():
    
    def __init__(self, matrix_as_list):
        self.matrix = copy.deepcopy(matrix_as_list)

    def get_occupied_seats(self):
        counter = 0
        for row in self.matrix:
            counter += row.count(OCCUPIED)

        return counter

    def get_empty_seats(self):
        counter = 0
        for row in self.matrix:
            counter += row.count(EMPTY)

        return counter

    def get_floor_seats(self):
        counter = 0
        for row in self.matrix:
            counter += row.count(FLOOR)

        return counter

    def get_cell_next_state_star1(self, i, j):
        current_state = self.matrix[i][j]
        neighbors = self.get_cell_neighbors_star1(i, j)
        full_seats = neighbors.count(OCCUPIED)

        if current_state == EMPTY:
            if full_seats == 0:
                return OCCUPIED

        elif current_state == OCCUPIED:
            if full_seats >= 4:
                return EMPTY

        return current_state

    def get_cell_next_state_star2(self, i, j):
        current_state = self.matrix[i][j]

        if current_state == FLOOR:
            return current_state

        neighbors = self.get_cell_neighbors_star2(i, j)
        full_seats = neighbors.count(OCCUPIED)

        if current_state == EMPTY:
            if full_seats == 0:
                return OCCUPIED

        elif current_state == OCCUPIED:
            if full_seats >= 5:
                return EMPTY

        return current_state

    def get_cell_neighbors_star1(self, i, j):
        neighbors = [
            self.matrix[i-1][j], self.matrix[i+1][j],
            self.matrix[i][j-1], self.matrix[i][j+1],
            self.matrix[i+1][j+1], self.matrix[i-1][j-1],
            self.matrix[i-1][j+1], self.matrix[i+1][j-1]
        ]

        return neighbors

    def get_cell_neighbors_star2(self, i, j):
        neighbors = []

        # Vertical up
        r = i-1
        neigh = FLOOR

        while neigh == FLOOR and r >= 0:
            neigh = self.matrix[r][j]
            r -= 1

        neighbors.append(neigh)

        # Vertical down
        r = i+1
        neigh = FLOOR

        while neigh == FLOOR and r < len(self.matrix):
            neigh = self.matrix[r][j]
            r += 1

        neighbors.append(neigh)

        # Horizontal left
        c = j-1
        neigh = FLOOR

        while neigh == FLOOR and c >= 0:
            neigh = self.matrix[i][c]
            c -= 1

        neighbors.append(neigh)

        # Horizontal right
        c = j+1
        neigh = FLOOR

        while neigh == FLOOR and c < len(self.matrix[0]):
            neigh = self.matrix[i][c]
            c += 1

        neighbors.append(neigh)

        # Diagonal left up
        r = i-1
        c = j-1
        neigh = FLOOR

        while neigh == FLOOR and r >= 0 and c >= 0:
            neigh = self.matrix[r][c]
            r -= 1
            c -= 1

        neighbors.append(neigh)

        # Diagonal right down
        r = i+1
        c = j+1
        neigh = FLOOR

        while neigh == FLOOR and r < len(self.matrix) and c < len(self.matrix[0]):
            neigh = self.matrix[r][c]
            r += 1
            c += 1

        neighbors.append(neigh)

        # Diagonal right up
        r = i-1
        c = j+1
        neigh = FLOOR

        while neigh == FLOOR and r >= 0 and c < len(self.matrix[0]):
            neigh = self.matrix[r][c]
            r -= 1
            c += 1

        neighbors.append(neigh)

        # Diagonal left down
        r = i+1
        c = j-1
        neigh = FLOOR

        while neigh == FLOOR and r < len(self.matrix) and c >= 0:
            neigh = self.matrix[r][c]
            r += 1
            c -= 1

        neighbors.append(neigh)

        return neighbors

    def pretty_print_noborder(self):
        for row in self.matrix[1:-1]:
            print(row[1:-1])

    def pretty_print_border(self):
        for row in self.matrix:
            print(row)

    def __repr__(self):
        return str(self.matrix)

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.matrix))

    def __eq__(self, other):
        if not isinstance(other, PlaneSeats):
            return False
        if len(self.matrix) != len(other.matrix):
            return False
        if len(self.matrix[0]) != len(other.matrix[0]):
            return False

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False

        return True

