from day_8.part1 import InstructionPtr, get_input
from utils import run


class InstructionPtr2(InstructionPtr):

    def __init__(self):
        super().__init__()
        self.full_list = []
        self.replaced = None
        self.replaced_index = None

    def add_instruction(self, instruction):
        super().add_instruction(instruction)
        self.full_list.append(instruction)

    def replace_instruction(self, index):
        if self.replaced:
            self.instructions[self.replaced_index] = self.replaced

        while self.full_list[index].group('action') == 'acc':
            index += 1

        new_action = 'nop' if self.full_list[index].group('action') == 'jmp' else 'jmp'
        value = self.full_list[index].group('value')
        self.replaced = self.instructions[index]
        self.replaced_index = index
        self.instructions[index] = self.parse_instruction(new_action, value)


def get_answer(input):
    program = InstructionPtr2()
    for item in input:
        program.add_instruction(item)

    terminated = False
    index = 0
    result = None
    while not terminated:
        program.replace_instruction(index)
        index += 1
        result, terminated = program.run()

    return result


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
