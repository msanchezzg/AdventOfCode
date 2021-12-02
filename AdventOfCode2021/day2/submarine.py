from dataclasses import dataclass


@dataclass
class Instruction:
    name: str
    n: int


class Submarine:
    movements = (
        'forward',
        'up',
        'down'
    )

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Submarine({self.x},{self.y})'

    def move(self, instruction):
        if instruction.name.lower() not in Submarine.movements:
            return
        func = getattr(self, f'move_{instruction.name.lower()}')
        func(instruction.n)

    def move_forward(self, n):
        self.x += n

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n


class Submarine2(Submarine):
    def __init__(self, x=0, y=0, aim=0):
        super().__init__(x, y)
        self.aim = 0

    def __repr__(self):
        return f'Submarine2({self.x},{self.y},{self.aim})'

    def move_forward(self, n):
        self.x += n
        self.y += self.aim * n

    def move_up(self, n):
        self.aim -= n

    def move_down(self, n):
        self.aim += n
