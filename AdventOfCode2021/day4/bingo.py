from collections import defaultdict


class BingoBoard:
    def __init__(self, board_as_list, num_rows, num_cols):
        self.board = board_as_list
        self.are_numbers_drawn = defaultdict(bool,{ k:False for k in self.board })
        self.win = False
        self.num_rows = num_rows
        self.num_cols = num_cols

    def __hash__(self):
        return hash((self.board, self.are_numbers_drawn))
    
    @classmethod
    def from_board_repr(cls, board_repr):
        board = []
        num_cols = 0
        num_rows = 0
        lines_split = [line for line in board_repr.split('\n') if line]
        for line in lines_split:
            row = [int(n) for n in line.split()]
            board += row
            num_rows += 1
            num_cols = len(row)
        return BingoBoard(board, num_rows, num_cols)

    def pretty_print(self):
        rows = [self.board[i:i+self.num_cols] for i in range(self.num_rows)]
        for r in rows:
            for n in r:
                if self.are_numbers_drawn[n]:
                    print(n, '*', end='\t')
                else:
                    print(n, end='\t')
            print()

    def number_draw(self, number):
        if number in self.are_numbers_drawn:
            self.are_numbers_drawn[number] = True
        self.check_win()

    def check_win(self):
        for i in range(self.num_rows):
            if self.check_win_row(i):
                self.win = True
                return
        for i in range(self.num_cols):
            if self.check_win_col(i):
                self.win = True
                return

    def check_win_row(self, index):
        row_index = index*self.num_cols
        for i in range(row_index, row_index+self.num_cols):
            n = self.board[i]
            if not self.are_numbers_drawn[n]:
                return False
        return True

    def check_win_col(self, index):
        for i in range(self.num_rows):
            n = self.board[index+i*self.num_cols]
            if not self.are_numbers_drawn[n]:
                return False
        return True

    def get_score(self):
        score = 0
        for number, is_drawn in self.are_numbers_drawn.items():
            if not is_drawn:
                score += number
        return score