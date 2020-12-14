from day_14.part1 import get_input
from utils import run


def set_value(key, value, mask, memory):
    value = int(value)
    key = int(key)
    main_mask = mask.replace('X', '0')
    key = key | int(main_mask, base=2)
    for submask in iterate_mask(mask):
        zeroes = submask.replace('X', '0')
        ones = submask.replace('X', '1')
        key = (key | int(zeroes, base=2)) & int(ones, base=2)
        memory[key] = value


def iterate_mask(mask):
    x_positions = [i for i, x in enumerate(mask) if x == 'X']
    mask = mask.replace('0', 'A')
    mask = mask.replace('1', 'A')
    mask = mask.replace('X', '0')
    mask = mask.replace('A', 'X')

    for i in range(2 ** len(x_positions)):
        binary = bin(i)[2:]
        submask = [x for x in mask]

        for j, pos in enumerate(x_positions):
            rev = len(binary) - 1 - j
            submask[pos] = binary[rev] if rev > -1 else '0'

        yield ''.join(submask)


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
