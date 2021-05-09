#!/usr/bin/python3

import math

from directions import Direction, Instruction


class Waypoint():

    def __init__(self, horizontal=0, vertical=0):
        self.hor_axis = horizontal
        self.vert_axis = vertical

    def move(self, instruction):
        """
        Move the waypoint in a given direction.
        """

        movements = {
            Direction.NORTH: lambda n: self.__move_vertically(n),
            Direction.SOUTH: lambda n: self.__move_vertically(-n),
            Direction.EAST: lambda n: self.__move_horizontally(n),
            Direction.WEST: lambda n: self.__move_horizontally(-n),
            Direction.RIGHT: lambda n: self.__rotate(-n),
            Direction.LEFT: lambda n: self.__rotate(+n),
        }

        movements.get(instruction.direction, lambda n: None)(instruction.n)

    def __move_horizontally(self, n):
        self.hor_axis += n

    def __move_vertically(self, n):
        self.vert_axis += n

    def __rotate(self, angle, radians=False):
        """
        Rotate the waypoint counterclockwise. To rotate clockwise, use a negative angle.
        """

        if not radians:
            angle = math.radians(angle)

        qx = math.cos(angle) * (self.hor_axis) - math.sin(angle) * (self.vert_axis)
        qy = math.sin(angle) * (self.hor_axis) + math.cos(angle) * (self.vert_axis)

        self.hor_axis = round(qx)
        self.vert_axis = round(qy)

    def __repr__(self):
        hor_direction = Direction.EAST if self.hor_axis >= 0 else Direction.WEST
        vert_direction = Direction.NORTH if self.vert_axis >= 0 else Direction.SOUTH

        return f'[{abs(self.vert_axis)} {vert_direction.value}, {abs(self.hor_axis)} {hor_direction.value}]'


class Ship():

    degrees = [
        [(0, 89), Direction.NORTH],
        [(90, 179), Direction.EAST],
        [(180, 269), Direction.SOUTH],
        [(270, 359), Direction.WEST]
    ]

    def __init__(self, horizontal=0, vertical=0, degrees=90):
        self.degrees = degrees
        self.hor_axis = horizontal
        self.vert_axis = vertical

    def move(self, instruction):
        movements = {
            Direction.NORTH: lambda n: self.__move_vertically(n),
            Direction.SOUTH: lambda n: self.__move_vertically(-n),
            Direction.EAST: lambda n: self.__move_horizontally(n),
            Direction.WEST: lambda n: self.__move_horizontally(-n),
            Direction.RIGHT: lambda n: self.__rotate(n),
            Direction.LEFT: lambda n: self.__rotate(-n),
            Direction.FORWARD: lambda n: self.__advance(n)
        }
        movements.get(instruction.direction, lambda n: None)(instruction.n)

    def __move_horizontally(self, n):
        self.hor_axis += n

    def __move_vertically(self, n):
        self.vert_axis += n

    def __rotate(self, degrees):
        self.degrees = (self.degrees + degrees) % 360
        if self.degrees < 0:
            self.degrees = 360 - self.degrees

    def __advance(self, n):
        pointing_direction = self.get_pointing_direction()
        self.move(Instruction(pointing_direction, n, from_enum=True))

    def get_pointing_direction(self):
        for deg, direction in Ship.degrees:
            if self.degrees >= deg[0] and self.degrees <= deg[1]:
                return direction

    def __repr__(self):
        hor_direction = Direction.EAST if self.hor_axis >= 0 else Direction.WEST
        vert_direction = Direction.NORTH if self.vert_axis >= 0 else Direction.SOUTH

        return f'[{abs(self.vert_axis)} {vert_direction.value}, {abs(self.hor_axis)} {hor_direction.value}, {self.degrees}º]'



class MovingShip():

    def __init__(self, horizontal=0, vertical=0):
        self.hor_axis = horizontal
        self.vert_axis = vertical
        self.waypoint = Waypoint(10, 1)

    def move(self, instruction):
        if instruction.direction != Direction.FORWARD:
            self.waypoint.move(instruction)
        else:
            self.hor_axis += instruction.n * self.waypoint.hor_axis
            self.vert_axis += instruction.n * self.waypoint.vert_axis

    def __repr__(self):
        hor_direction = Direction.EAST if self.hor_axis >= 0 else Direction.WEST
        vert_direction = Direction.NORTH if self.vert_axis >= 0 else Direction.SOUTH

        return f'[{abs(self.vert_axis)} {vert_direction.value}, {abs(self.hor_axis)} {hor_direction.value}]'
