#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
from typing import Tuple


class Node2:
    all_nodes = []

    def __init__(self, children: Tuple[int], metadata: Tuple[int]):
        self.id = len(Node2.all_nodes)
        self.children = children
        self.metadata = metadata
        self.value = self._get_value()

        Node2.all_nodes.append(self)

    def __repr__(self):
        return f'Node(id={self.id} children={self.children}, metadata={self.metadata}, value={self.value})'

    def _get_value(self):
        value = 0
        if len(self.children) == 0:
            return sum(self.metadata)

        for meta in self.metadata:
            position = meta - 1
            if 0 <= position and position < len(self.children):
                child_id = self.children[position]
                child_node  = Node2.get_node(child_id)
                if child_node:
                    value += child_node.value
        return value

    @staticmethod
    def get_node(id):
        for node in Node2.all_nodes:
            if node.id == id:
                return node
        return None


def get_node_from_descr(nodes_descr: str, start_index: int =0):
    nchildren = nodes_descr[start_index]
    nmetadata = nodes_descr[start_index+1]
    children = []
    metadata = []

    if nchildren != 0:
        for _ in range(nchildren):
            child_node = get_node_from_descr(nodes_descr, start_index+2)
            children.append(child_node.id)

    for m in range(nmetadata):
        meta = nodes_descr[start_index + 2 + m]
        metadata.append(meta)

    last_index = start_index + 1 + nmetadata
    node = Node2(tuple(children), tuple(metadata))

    # Delete node from nodes_descr
    for _ in range(start_index, last_index+1):
        nodes_descr.pop(start_index)

    return node


def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.read()

    nodes_descr = [int(x) for x in lines.split()]
    get_node_from_descr(nodes_descr)

    print('Nodes:')
    metadata_sum = 0
    for node in Node2.all_nodes:
        metadata_sum += sum(node.metadata)
        print(f'\t{node}')

    print()
    print('PART 1')
    print(f'Sum of metadata = {metadata_sum}')

    print()
    print('PART 2')
    node_A = Node2.get_node(len(Node2.all_nodes) - 1)
    print(f"Value of node 'A' (node with biggest id: {node_A.id}) = {node_A.value}")


if __name__ == "__main__":
    main(sys.argv[1])
