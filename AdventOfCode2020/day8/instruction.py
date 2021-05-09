
class Instruction():
    """
    Class to represent the instructions of a console.
    """

    next_instruction = 0
    accumulator = 0

    def __init__(self, operation, argument, index):
        self.op = operation
        self.arg = argument
        self.index = index

    @staticmethod
    def reset_state():
        Instruction.next_instruction = 0
        Instruction.accumulator = 0

    def execute(self):
        if self.op == 'acc':
            Instruction.accumulator += self.arg
            Instruction.next_instruction += 1
        elif self.op == 'jmp':
            Instruction.next_instruction += self.arg
        elif self.op == 'nop':
            Instruction.next_instruction += 1

    def change_operation(self):
        changes = {'jmp': 'nop', 'nop': 'jmp'}
        self.op = changes.get(self.op, self.op)

    def __hash__(self):
        return hash((self.op, self.arg, self.index))

    def __eq__(self, other):
        return self.op == other.op and self.arg == other.arg and self.index == other.index

    def __repr__(self):
        return str([self.op, self.arg, self.index])
