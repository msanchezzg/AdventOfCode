#!/usr/bin/python3


class Stack():
    """
    This class represents a stack, a LIFO structure.
    """

    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def top(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop(-1)

    def is_empty(self):
        return self.items == []

    def __repr__(self):
        return str(self.items)