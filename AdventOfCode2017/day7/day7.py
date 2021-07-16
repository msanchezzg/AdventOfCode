#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
import re
from anytree import NodeMixin, RenderTree


class Program(NodeMixin):
    def __init__(self, name, weight=0, parent=None, children=None):
        self.name = name
        self.weight = weight
        self.parent = parent
        if children:
            self.children = children

    def __repr__(self):
        return str(self.__dict__)

    def print_subtree(self):
        for pre, _, node in RenderTree(self):
            treestr = u"%s%s" % (pre, node.name)
            print(treestr.ljust(8), node.weight)

    def get_subtree_weight(self):
        if self.children is None:
            return self.weight

        weight = self.weight
        for child in self.children:
            weight += child.get_subtree_weight()
        return weight

    def get_unbalanced_node(self):
        if self.children is None:
            return None, -1

        children_total_weights = [child.get_subtree_weight() for child in self.children]
        min_weight = min(children_total_weights)
        weight_diffs = [w-min_weight for w in children_total_weights]
        is_balanced = True
        unbalanced_node = None
        for i,w in enumerate(weight_diffs):
            if w != 0:
                unbalanced_node = self.children[i]
                unbalanced_weight = w
                is_balanced = False

        if is_balanced:
            return None, -1

        unbalanced_child, balanced_weight = unbalanced_node.get_unbalanced_node()
        if unbalanced_child is None:
            balanced_weight = unbalanced_node.weight - unbalanced_weight
            return unbalanced_node, balanced_weight
        else:
            return unbalanced_child, balanced_weight



def update_parent(programs_by_name, parent_name, children_names):
    children_programs = []
    parent_program = programs_by_name[parent_name]
    for child_name in children_names:
        child_program = programs_by_name.get(child_name, None)
        if child_program is None:
            child_program = Program(name=child_name)
            programs_by_name[child_name] = child_program
        child_program.parent = parent_program
        children_programs.append(child_program)
    parent_program.children = children_programs


def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.read().split('\n')

    programs_by_name = {}
    line_format = re.compile(r'(.+) \((\d+)\)( -> (.*))?')
    for line in lines:
        match = line_format.match(line)
        name, weight, _, children = match.groups()
        weight = int(weight)
        if children is not None:
            children = [c.strip() for c in children.split(',')]

        if name in programs_by_name:
            programs_by_name[name].weight = weight
        else:
            programs_by_name[name] = Program(name, weight)

        if children is not None:
            update_parent(programs_by_name, name, children)

    root = programs_by_name[name].root
    # root.print_subtree()

    print('PART 1')
    print(f'Root program = {root.name}')

    print('\n-----------------------------------\n')

    unbalanced_program, balanced_weight = root.get_unbalanced_node()

    print('PART 2')
    print(f'Unbalanced program: {unbalanced_program.name}')
    print(f'Program current weight = {unbalanced_program.weight}, weight to balance the tree = {balanced_weight}')



if __name__ == "__main__":
    main(sys.argv[1])
