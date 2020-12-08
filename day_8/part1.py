import re

from utils import run

rx_data = re.compile(r'^(?P<action>jmp|acc|nop) \+?(?P<value>-?\d+)$', re.MULTILINE)


def get_input(content):
    return rx_data.finditer(content)


class InstructionPtr:
    def __init__(self):
        self.instructions = []
        self.visited = set()

    def add_instruction(self, instruction):
        self.instructions.append(self.parse_instruction(
            instruction.group('action'),
            instruction.group('value'),
        ))

    def parse_instruction(self, action, value):
        if action == 'nop':
            return 1, 0
        if action == 'acc':
            return 1, int(value)
        if action == 'jmp':
            return int(value), 0

    def run(self):
        index = 0
        value = 0

        while index not in self.visited and index < len(self.instructions):
            mod_index, mod_value = self.instructions[index]
            self.visited.add(index)
            index += mod_index
            value += mod_value

        self.visited = set()
        return value, index >= len(self.instructions)


def get_answer(input):
    program = InstructionPtr()
    for item in input:
        program.add_instruction(item)

    result, terminated = program.run()
    return result


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
