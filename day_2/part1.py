import os
import re
from time import time

from utils import read_file

rx_data = re.compile(r'^(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<pass>\w+)$', re.MULTILINE)


def get_input():
    content = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    return rx_data.finditer(content)


def get_answer(input):
    good = 0
    for item in input:
        min_count = int(item.group('min'))
        max_count = int(item.group('max'))
        search_char = item.group('char')
        matches = len([c for c in item.group('pass') if c == search_char])

        if min_count <= matches <= max_count:
            good += 1
    return good


if __name__ == '__main__':
    t0 = time()
    print(f'answer: {get_answer(get_input())}')
    print(f'{time() - t0}')

