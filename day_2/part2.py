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
        pos1 = int(item.group('min')) - 1
        pos2 = int(item.group('max')) - 1
        search_char = item.group('char')
        passwd = item.group('pass')

        if (passwd[pos1] == search_char) != (passwd[pos2] == search_char):
            good += 1
    return good


if __name__ == '__main__':
    t0 = time()
    print(f'answer: {get_answer(get_input())}')
    print(f'{time() - t0}')

