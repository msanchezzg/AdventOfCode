#!/usr/bin/python3
#-*- coding: utf-8 -*-

class Node():
    '''
    This class represents a node of a Doubly Linked List.
    '''

    def __init__(self, value=None, prev=None, nextt=None):
        self.value = value
        self.prev = prev
        self.next = nextt

    def pop_next(self):
        current_next = self.next
        self.next = current_next.next
        self.next.prev = self
        return current_next

    def add_next_node(self, node):
        node.next = self.next
        node.prev = self
        if self.next:
            self.next.prev = node
        self.next = node

    def __repr__(self):
        return str(self.value)
