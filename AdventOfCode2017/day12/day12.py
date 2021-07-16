#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
import re


def get_all_neighbors(nodes_neighbors, node, visited_nodes=None):
    all_neighbors = set()
    if visited_nodes is None:
        visited_nodes = set()
    direct_neighbors = nodes_neighbors[node]
    visited_nodes.add(node)
    for neigh in direct_neighbors:
        all_neighbors.add(neigh)
        if neigh not in visited_nodes:
            visited_nodes.add(neigh)
            neighs = get_all_neighbors(nodes_neighbors, neigh, visited_nodes)
            all_neighbors.update(neighs)

    return all_neighbors


def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.read().split('\n')

    line_format = re.compile(r'(.*) <-> (.*)')
    nodes_neighbors = {}
    for line in lines:
        node, neighbors = line_format.match(line).groups()
        node_number = int(node)
        neighbors_list = [int(n) for n in neighbors.split(',')]
        nodes_neighbors[node_number] = neighbors_list

    neighbors0 = get_all_neighbors(nodes_neighbors, 0)
    print('PART 1')
    print(f'Number of nodes in group 0 = {len(neighbors0)}')
    print(neighbors0)

    print('\n--------------------------------------\n')

    print('PART 2')
    groups = []
    nodes_in_group = set()
    for node in nodes_neighbors:
        if node in nodes_in_group:
            continue
        neighbors = get_all_neighbors(nodes_neighbors, node)
        groups.append(neighbors)
        nodes_in_group.update(neighbors)

    print(f'Number of different groups = {len(groups)}')
    print('List of groups:')
    for group in groups:
        print(f'\t{group}')


if __name__ == "__main__":
    main(sys.argv[1])
