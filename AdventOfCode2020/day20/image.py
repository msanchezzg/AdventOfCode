#!/usr/bin/python3
#-*- coding: utf-8 -*-



class Matrix:

    def __init__(self, matrix):
        tuple_matrix = []
        for row in matrix:
            tuple_matrix.append(tuple(row))
        self.matrix = tuple(tuple_matrix)

    def pretty_print(self):
        for row in self.matrix:
            print(row)

    def get_nrows(self):
        return len(self.matrix)

    def get_ncols(self):
        return len(self.matrix[0])

    def get_row(self, index, reverse=False):
        if reverse:
            return self.matrix[index][::-1]
        return self.matrix[index]

    def get_column(self, index, reverse=False):
        border = [row[index] for row in self.matrix]
        if reverse:
            return border[::-1]
        return border

    def count_value(self, value):
        total = 0
        for row in self.matrix:
            total += row.count(value)
        return total

    def flip_vertically(self, inplace=False):
        matrix = []
        for row in self.matrix:
            matrix.append(tuple(row[::-1]))
        if inplace:
            self.matrix = tuple(matrix)
        else:
            return Matrix(matrix)

    def flip_horizontally(self, inplace=False):
        m = self.matrix[::-1]
        matrix = []
        for row in m:
            matrix.append(tuple(row))
        if inplace:
            self.matrix = tuple(matrix)
        else:
            return Matrix(matrix)

    def rotate_clockwise(self, inplace=False):
        m = list(zip(*self.matrix[::-1]))
        matrix = []
        for row in m:
            matrix.append(tuple(row))
        if inplace:
            self.matrix = tuple(matrix)
        else:
            return Matrix(matrix)

    def rotate_counterclockwise(self, inplace=False):
        m = list(zip(*self.matrix))[::-1]
        matrix = []
        for row in m:
            matrix.append(tuple(row))
        if inplace:
            self.matrix = tuple(matrix)
        else:
            return Matrix(matrix)

    def get_all_rotations(self):
        rotations = set()
        for _ in range(4):
            rotations.add(Matrix(self.matrix))
            rotations.add(self.flip_vertically())
            rotations.add(self.flip_horizontally())
            
            self.rotate_clockwise(inplace=True)
        return rotations

    def get_submatrix(self, first_row, last_row, first_col, last_col):
        submatrix = []
        for row in self.matrix[first_row:last_row+1]:
            submatrix.append(row[first_col:last_col+1])
        return Matrix(submatrix)


class Image():

    def __init__(self, pixels_matrix, id):
        self.id = id
        self.pixels_matrix = pixels_matrix
        self.top_neigh = None
        self.bottom_neigh = None
        self.left_neigh = None
        self.right_neigh = None

    def reset_neighs(self):
        if self.top_neigh is not None:
            self.top_neigh.bottom_neigh = None
            self.top_neigh = None
        if self.bottom_neigh is not None:
            self.bottom_neigh.top_neigh = None
            self.bottom_neigh = None
        if self.left_neigh is not None:
            self.left_neigh.right_neigh = None
            self.left_neigh = None
        if self.right_neigh is not None:
            self.right_neigh.left_neigh = None
            self.right_neigh = None

    def count_pixels(self, pixel_value):
        return self.pixels_matrix.count_value(pixel_value)

    def pretty_print_pixels(self):
        self.pixels_matrix.pretty_print()

    def pretty_print_neighs(self):
        top = self.top_neigh.id if self.top_neigh is not None else None
        bottom = self.bottom_neigh.id if self.bottom_neigh is not None else None
        left = self.left_neigh.id if self.left_neigh is not None else None
        right = self.right_neigh.id if self.right_neigh is not None else None
        print('{', self.id, ':', top, bottom, left, right, '}')

    def get_top_border(self, reverse=False):
        return self.pixels_matrix.get_row(0, reverse)

    def get_bottom_border(self, reverse=False):
        return self.pixels_matrix.get_row(-1, reverse)

    def get_left_border(self, reverse=False):
        return self.pixels_matrix.get_column(0, reverse)

    def get_right_border(self, reverse=False):
        return self.pixels_matrix.get_column(-1, reverse)

    def match_top_border(self, image):
        if self.get_top_border() == image.get_bottom_border():
            self.top_neigh = image
            image.bottom_neigh = self
            return True
        return False

    def match_bottom_border(self, image):
        if self.get_bottom_border() == image.get_top_border():
            self.bottom_neigh = image
            image.top_neigh = self
            return True
        return False

    def match_left_border(self, image):
        if self.get_left_border() == image.get_right_border():
            self.left_neigh = image
            image.right_neigh = self
            return True
        return False

    def match_right_border(self, image):
        if self.get_right_border() == image.get_left_border():
            self.right_neigh = image
            image.left_neigh = self
            return True
        return False
