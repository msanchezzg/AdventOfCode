#-*- coding: utf-8 -*-


from copy import deepcopy


BUG = '#'
EMPTY = '.'

class Matrix:
    def __init__(self, data):
        self.data = data

    def __hash__(self):
        immutable = tuple([tuple(row) for row in self.data])
        return hash(immutable)

    def immutable(self):
        immutable = tuple([tuple(row) for row in self.data])
        return immutable

    def pretty_print(self):
        for row in self.data:
            print(row)

    def in_range(self, x, y):
        if x < 0:
            return False
        if x >= len(self.data):
            return False
        if y < 0:
            return False
        if y >= len(self.data[0]):
            return False
        return True

    def get_4_neighbors(self, x, y):
        neighbors = []

        neigh_coordinates = (
            (x, y-1),   # Up
            (x, y+1),   # Down
            (x-1, y),   # Left
            (x+1, y)    #Right
        )

        for neigh_x, neigh_y in neigh_coordinates:
            if self.in_range(neigh_x, neigh_y):
                neighbors.append(self.data[neigh_x][neigh_y])
        return neighbors

    def get_new_state(self, x, y):
        neighbors = self.get_4_neighbors(x, y)
        if self.data[x][y] == BUG:
            if neighbors.count(BUG) == 1:
                return BUG
            return EMPTY
        else:
            if neighbors.count(BUG) in [1,2]:
                return BUG
            return EMPTY

    def evolve(self):
        new_data = deepcopy(self.data)
        for x in range(len(self.data)):
            for y in range(len(self.data[0])):
                new_state = self.get_new_state(x, y)
                new_data[x][y] = new_state
        return Matrix(new_data)

    def get_cell_biodiversity(self, x, y):
        if self.data[x][y] == EMPTY:
            return 0
        nrows = len(self.data)
        return 2**((x*nrows)+y)

    def get_total_biodiversity(self):
        biodiversity = 0
        for x in range(len(self.data)):
            for y in range(len(self.data[0])):
                biodiversity += self.get_cell_biodiversity(x, y)
        return biodiversity
