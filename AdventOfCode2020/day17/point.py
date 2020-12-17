#!/usr/bin/python3
#-*- coding: utf-8 -*-

from enum import Enum


class PointState(Enum):
    """
    Enum class that represents the states of a point.
    """

    ACTIVE = '#'
    INACTIVE = '.'


class Point4D():
    """
    Class that represents a point in a 4-dimesional space.

    Attributes:
    x : int
        Point's coordinate in the x axis.
    y : int
        Point's coordinate in the y axis.
    z : int
        Point's coordinate in the z axis.
    w : int
        Point's coordinate in the w axis.
    """

    def __init__(self, x=0, y=0, z=0, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __eq__(self, other):
        if not isinstance(other, Point4D):
            return False

        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w

    def __hash__(self):
        return hash((self.x, self.y, self.z, self.w))

    def __repr__(self):
        return str((self.x, self.y, self.z, self.w))

    def get_neighbors(self):
        neighbors = []
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                for z in [-1,0,1]:
                    for w in [-1,0,1]:
                        neighbors.append(Point4D(self.x+x, self.y+y, self.z+z, self.w+w))

        neighbors.remove(self)
        return neighbors