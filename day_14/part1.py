import re

from utils import run

rx_data = re.compile(r'^(?:(?:mem\[(?P<key>\d+)\] = (?P<value>\d+))|mask = (?P<mask>\w+))$', re.MULTILINE)


def get_input(content):
    return rx_data.finditer(content)


def set_value(key, value, mask, memory):
    value = int(value)
    key = int(key)

    if not mask:
        memory[key] = value
        return

    zeroes = mask.replace('X', '0')
    ones = mask.replace('X', '1')
    value = (value | int(zeroes, base=2)) & int(ones, base=2)
    memory[key] = value


def get_answer(input):
    memory = {}
    mask = None

    for line in input:
        if line.group('mask'):
            mask = line.group('mask')
        else:
            key = line.group('key')
            value = line.group('value')
            set_value(key, value, mask, memory)

    return sum(memory.values())


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
