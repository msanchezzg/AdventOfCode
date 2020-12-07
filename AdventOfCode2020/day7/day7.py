#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import re
import networkx as nx


def get_weight(bags_connections, parent_node): 
    number_of_childs = len(bags_connections[parent_node])
    if number_of_childs == 0:
        return 0

    childs_weight = 0
    for child, weight in bags_connections[parent_node]:
        weight_of_child = get_weight(bags_connections, child)
        childs_weight += (weight*weight_of_child)
        childs_weight += weight

    return childs_weight



def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    COLOR_SEARCH = 'shiny gold'
    line_format = r'(.*) bags contain (.*).$'
    child_format = r'(\d*)\s?(.*) bags?'
    bags_connections = {}
    colors = set()
    total_paths = 0

    for line in lines:
        matches = re.match(line_format, line).groups()
        parent_color, childs = matches
        colors.add(parent_color)
        child_list = []

        for child in childs.split(', '):
            matches = re.match(child_format, child).groups()
            child_weight, child_color = matches
            child_weight = int(child_weight) if child_weight else 0
            child_list.append((child_color, child_weight)) if child_color != 'no other' else None

        bags_connections[parent_color] = child_list

    bags_digraph = nx.DiGraph()
    for color in bags_connections:
        bags_digraph.add_node(color)
        for conn, _ in bags_connections[color]:
            bags_digraph.add_edge(color, conn)

    colors.remove(COLOR_SEARCH)
    for color in colors:
        try:
            path = nx.shortest_path(bags_digraph, source=color, target=COLOR_SEARCH)
            # print(f"Path from '{color}' to '{COLOR_SEARCH}': {path}")
            total_paths += 1
        except nx.exception.NetworkXNoPath:
            continue
    
    # print()
    print('PART 1')
    print(f"Total paths from a color to '{COLOR_SEARCH}' = {total_paths}")
    print('\n--------------------------------------------------\n')
    print('PART 2')
    total_bags = get_weight(bags_connections, COLOR_SEARCH)
    print(f"Total number of bags inside a '{COLOR_SEARCH}' bag = {total_bags}")



if __name__ == "__main__":
    main(sys.argv[1])
