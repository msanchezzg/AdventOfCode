# -*- coding: utf-8 -*-


import argparse
from bingo import BingoBoard


def main(input_file):

    with open(input_file, "r") as f:
        lines = f.read()

    numbers_to_draw, *boards_reprs = [x for x in lines.split('\n\n') if x]
    numbers_to_draw = [int(x) for x in numbers_to_draw.split(',')]
    boards = [BingoBoard.from_board_repr(b) for b in boards_reprs]
    first_winner_drawn_number = -1
    first_winner_board = None
    winner_drawn_number = -1
    winner_board = None
    winners_count = 0

    for number in numbers_to_draw:
        for board in boards:
            if board.win:
                continue
            board.number_draw(number)
            if board.win:
                winner_drawn_number = number
                winner_board = board
                winners_count += 1
                if first_winner_board is None:
                    first_winner_drawn_number = number
                    first_winner_board = board
        if winners_count == len(boards):
            break

    print('PART 1')
    print(f'First winner drawn number: {first_winner_drawn_number}')
    print(f'First winner board score: {first_winner_board.get_score()}')
    print(f'Product = {first_winner_drawn_number * first_winner_board.get_score()}')

    print('\n----------------------------------------------\n')
    print('PART 2')
    print(f'Last winner drawn number: {winner_drawn_number}')
    print(f'Last winner board score: {winner_board.get_score()}')
    print(f'Product = {winner_drawn_number * winner_board.get_score()}')        


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Python3 template file for Advent of Code problems"
    )
    parser.add_argument("input_file", type=str, help="File with problem input")

    args = parser.parse_args()
    main(args.input_file)
