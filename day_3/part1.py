import os
from time import time

from utils import read_file


def get_input():
    content = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    return content.split('\n')


def get_answer(input):
    x = 3
    count = 0
    for line in input[1:]:
        if not len(line):
            continue
        count += 1 if line[x % len(line)] == '#' else 0
        x += 3

    return count


if __name__ == '__main__':
    t0 = time()
    print(f'answer: {get_answer(get_input())}')
    print(f'{time() - t0}')

