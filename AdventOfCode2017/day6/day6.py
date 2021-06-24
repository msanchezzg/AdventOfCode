#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys


def redistrubute_memory(memory):
    memory_len = len(memory)

    # Get bank with more blocks
    max_blocks = -1
    max_blocks_index = -1
    for i, bank in enumerate(memory):
        if bank > max_blocks:
            max_blocks = bank
            max_blocks_index = i

    # Redistribute those banks
    memory[max_blocks_index] = 0
    allocate_index = (max_blocks_index + 1) % memory_len
    for _ in range(max_blocks):
        memory[allocate_index] += 1
        allocate_index = (allocate_index + 1) % memory_len


def main(input_file):

    with open(input_file, 'r') as f:
        memory = [int(x) for x in f.read().split()]

    history = set()
    iterations = 0
    repeated_state = None

    while True:
        iterations += 1
        redistrubute_memory(memory)
        memory_state = tuple(memory)
        # print(f'{iterations}:\t {memory_state}')
        if memory_state in history:
            repeated_state = memory_state
            break
        history.add(memory_state)

    print('PART 1')
    print(f'State repeated: {repeated_state}')
    print(f'State repeated after {iterations} iterations')

    print('\n----------------------------------------\n')

    iterations = 0
    while True:
        iterations += 1
        redistrubute_memory(memory)
        memory_state = tuple(memory)
        if memory_state == repeated_state:
            break

    print('PART 2')
    print(f'State re-repeated after {iterations} iterations')


if __name__ == "__main__":
    main(sys.argv[1])
