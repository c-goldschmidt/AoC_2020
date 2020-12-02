import itertools
import os
from time import time

from utils import read_file


def get_list():
    content = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    return content.split('\n')


def get_answer(input):
    input.sort(reverse=True)
    for x, y in itertools.product(input, input):
        x = int(x)
        y = int(y)

        if x + y == 2020:
            return x * y


if __name__ == '__main__':
    t0 = time()
    print(f'answer: {get_answer(get_list())}')
    print(f'{time() - t0}')

