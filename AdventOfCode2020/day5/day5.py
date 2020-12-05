#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import math


class PlaneSeat():
    NUM_OF_ROWS = 128
    NUM_OF_COLS = 8

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.id = row * PlaneSeat.NUM_OF_COLS + col

    @classmethod
    def from_binary_partition(cls, binary_part):
        row = PlaneSeat.__parse_row_chars(binary_part[0:7])
        col = PlaneSeat.__parse_col_chars(binary_part[7:])
        return PlaneSeat(row, col)

    @staticmethod
    def __parse_row_chars(binary_part):
        seat_range = list(range(0, PlaneSeat.NUM_OF_ROWS))
        characters = {
            'F': (lambda range: range[0:len(range)//2]),
            'B': (lambda range: range[math.ceil(len(range)/2):])
        }
        for letter in binary_part:
            seat_range = characters[letter](seat_range)

        return seat_range[0]

    @staticmethod
    def __parse_col_chars(binary_part):
        seat_range = list(range(0, PlaneSeat.NUM_OF_COLS))
        characters = {
            'L': (lambda range: range[0:len(range)//2]),
            'R': (lambda range: range[math.ceil(len(range)/2):])
        }
        for letter in binary_part:
            seat_range = characters[letter](seat_range)

        return seat_range[0]

    @staticmethod
    def get_all_seats():
        seats = []
        for row in range(0, PlaneSeat.NUM_OF_ROWS):
            for col in range(0, PlaneSeat.NUM_OF_COLS):
                seats.append(PlaneSeat(row, col))
        return seats


    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __gt__(self, other):
        return self.id > other.id

    def __lt__(self, other):
        return self.id > other.id

    def __repr__(self):
        return str([self.row, self.col, self.id])



def main(input_file):
    with open(input_file, 'r') as f:
        lines = [l for l in f.read().split('\n') if l]

    seats_ids = []

    # Star 1: get the highest ID of read seats
    print('PART 1')
    for l in lines:
        seat = PlaneSeat.from_binary_partition(l)
        seats_ids.append(seat.id)
        # print(f"line '{l}' => seat row={seat.row},\tcol={seat.col},\tid={seat.id}")

    # print()
    
    print(f'Highest ID = {max(seats_ids)}')

    print('\n--------------------------------------------------------\n')

    # Star 2: get empty seat ID between two seats
    print('PART 2')

    seats_ids.sort()
    for i in range(0, len(seats_ids)-1):
        s1 = seats_ids[i]
        s2 = seats_ids[i+1]
        separation = s2 - s1
        if separation != 1:
            print(f'My seat ID = {s1 + 1}')
            break


if __name__ == "__main__":
    main(sys.argv[1])
