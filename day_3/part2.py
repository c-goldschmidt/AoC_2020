import operator
import os
from functools import reduce
from time import time

from utils import read_file


def get_input():
    content = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    return content.split('\n')


def get_for_slope(input, y_slope, x_slope):
    count = 0
    y_index = y_slope
    for line in input[x_slope::x_slope]:
        if not line:
            continue

        count += 1 if line[y_index % len(line)] == '#' else 0
        y_index += y_slope
    return count


def get_answer(input):
    return reduce(operator.mul, (
        get_for_slope(input, 1, 1),
        get_for_slope(input, 3, 1),
        get_for_slope(input, 5, 1),
        get_for_slope(input, 7, 1),
        get_for_slope(input, 1, 2),
     ), 1)


if __name__ == '__main__':
    t0 = time()
    print(f'answer: {get_answer(get_input())}')
    print(f'{time() - t0}')

