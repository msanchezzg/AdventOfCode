#!//usr/bin/python3
#-*- coding: utf-8 -*-


import sys
import re


neighs_increments = {
    r'^nw(.*)$': (-1, -1), r'^ne(.*)$': (-1, +1),
    r'^w(.*)$': (0, -2),   r'^e(.*)$': (0, +2),
    r'^sw(.*)$': (+1, -1), r'^se(.*)$': (+1, +1)
}

def get_neighs(cell):
    neighs = []
    for _, increment in neighs_increments.items():
        neighs.append((cell[0]+increment[0], cell[1]+increment[1]))

    return neighs

def get_cell_index(path, current_cell):
    if path == "":
        return current_cell

    for coord, increment in neighs_increments.items():
        match = re.match(coord, path)
        if match:
            row = current_cell[0] + increment[0]
            col = current_cell[1] + increment[1]
            rest_path = match.groups()[0]
            return get_cell_index(rest_path, (row, col))

def add_neighs(source_cells_group, target_cells_group, check_cells_group):
    for cell in source_cells_group:
        for neigh in get_neighs(cell):
            if neigh not in check_cells_group:
                target_cells_group.add(neigh)



def main(input_file):

    with open(input_file, 'r') as f:
        operations = f.read().split('\n')

    black_cells = set()
    white_cells = set()
    initial_cell = (0, 0)

    for op in operations:
        target_cell = get_cell_index(op, initial_cell)
        if target_cell in black_cells:
            black_cells.remove(target_cell)
            white_cells.add(target_cell)
        else:
            black_cells.add(target_cell)
            if target_cell in white_cells:
                white_cells.remove(target_cell)

    print('PART 1')
    print(f'Number of black cells = {len(black_cells)}')

    print('\n------------------------------------------\n')

    print('PART 2')

    new_black_cells = set()
    new_white_cells = set()

    # Add missing neighbors
    add_neighs(black_cells, white_cells, black_cells)
    add_neighs(white_cells, new_white_cells, black_cells)
    white_cells.union(new_white_cells)

    # Simulation
    days = 100
    for i in range(1, days+1):
        new_black_cells.clear()
        new_white_cells.clear()

        for cell in black_cells:
            black_neighs = 0
            for neigh in get_neighs(cell):
                if neigh in black_cells:
                    black_neighs += 1
            if black_neighs == 0 or black_neighs > 2:
                new_white_cells.add(cell)
            else:
                new_black_cells.add(cell)

        for cell in white_cells:
            black_neighs = 0
            for neigh in get_neighs(cell):
                if neigh in black_cells:
                    black_neighs += 1
            if black_neighs == 2:
                new_black_cells.add(cell)
            else:
                new_white_cells.add(cell)

        black_cells.clear()
        black_cells.update(new_black_cells)
        white_cells.clear()
        white_cells.update(new_white_cells)

        print(f'Day {i}: Black = {len(black_cells)}, White = {len(white_cells)}, Total =  {len(white_cells)+len(black_cells)}')

        # Add neighbors of black cells
        add_neighs(black_cells, white_cells, black_cells)


if __name__ == "__main__":
    main(sys.argv[1])
