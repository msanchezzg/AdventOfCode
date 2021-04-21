#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
from copy import copy
import re


POT_EMPTY = '.'
POT_FULL = '#'


def add_borders(pots_states, initial_pot_index):
    empty_border = [POT_EMPTY, POT_EMPTY]
    while pots_states[0:2] != empty_border:
        pots_states.insert(0, POT_EMPTY)
        initial_pot_index += 1
    # Right
    while pots_states[-2:] != empty_border:
        pots_states.append(POT_EMPTY)

    return initial_pot_index

def get_neighbors(pots_states, pot_index):
    pot_neighs = []
    for i in range(-2, 3):
        neigh_index = pot_index + i
        if 0 <= neigh_index < len(pots_states):
            pot_neighs.append(pots_states[neigh_index])
        else:
            pot_neighs.append(POT_EMPTY)
    return tuple(pot_neighs)


def main(input_file):

    with open(input_file, 'r') as f:
        inital_state, *notes = f.read().split('\n')
    
    notes_format = re.compile(r'^([\.#]*) => ([\.#])$')
    notes_by_pots_descr = {}
    for note in notes[1:]:
        nearby_pots, next_state = notes_format.match(note).groups()
        notes_by_pots_descr[tuple(nearby_pots)] = next_state

    generations = 20
    pots_states = list(inital_state.split(': ')[1])
    initial_pot_index = 0

    # Add empty pots to left and right if the borders are full.
    # There must always be two empty pots at the borders.
    initial_pot_index = add_borders(pots_states, initial_pot_index)

    for gen in range(generations):
        future_states = []

        # Change the pots states
        for pot_index, _ in enumerate(pots_states):
            pot_neighs = get_neighbors(pots_states, pot_index)
            next_state = notes_by_pots_descr.get(pot_neighs, POT_EMPTY)
            future_states.append(next_state)

        initial_pot_index = add_borders(future_states, initial_pot_index)

        # Copy pots_states into future_states
        pots_states = copy(future_states)

        # print(f'Generation {g+1}:\t{pots_states}')

    pots_plants_indeces = []
    for i, pot in enumerate(pots_states):
        if pot == POT_FULL:
            pots_plants_indeces.append(i-initial_pot_index)

    print('PART 1')
    print(f'Final pots state: {pots_states}')
    print(f'Initial pot index: {initial_pot_index}')
    print(f'Pots containing plants: {pots_plants_indeces}')
    print(f'Sum of all plants indeces = {sum(pots_plants_indeces)}')


if __name__ == "__main__":
    main(sys.argv[1])
