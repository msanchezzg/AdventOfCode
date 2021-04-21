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

def get_pots_indeces_sum(pots_states, initial_pot_index):
    pots_plants_indeces_sum = 0
    for i, pot in enumerate(pots_states):
        if pot == POT_FULL:
            real_pot_index = i-initial_pot_index
            pots_plants_indeces_sum += real_pot_index

    return pots_plants_indeces_sum

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

    generations = 50000000000
    pots_states = list(inital_state.split(': ')[1])
    initial_pot_index = 0

    # Add empty pots to left and right if the borders are full.
    # There must always be two empty pots at the borders.
    initial_pot_index = add_borders(pots_states, initial_pot_index)    

    pots_indeces_sums_differences = []
    pots_plants_indeces_sum_prev = 0
    gen = 0
    sums_difference = 0
    current_sum = 0

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

        # Compute sum of indices of pots containing plants
        current_sum = get_pots_indeces_sum(pots_states, initial_pot_index)

        # Compute difference of current sum with previous state's
        sum_diff = current_sum - pots_plants_indeces_sum_prev

        # Check if there is a pattern in the differences
        if len(pots_indeces_sums_differences) > 2:
            if sum_diff == pots_indeces_sums_differences[-1] and \
                sum_diff == pots_indeces_sums_differences[-2]:
                sums_difference = sum_diff
                break

        pots_indeces_sums_differences.append(sum_diff)
        pots_plants_indeces_sum_prev = current_sum


    print('PART 2')
    remaining_generations = generations - gen - 1
    print(f'Sum of all plants indeces = {current_sum + sums_difference * remaining_generations}')


if __name__ == "__main__":
    main(sys.argv[1])
