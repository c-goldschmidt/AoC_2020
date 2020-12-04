import os
import re
from time import time

from utils import read_file

rx_key_value = re.compile(r'(?P<key>\w{3})')


def get_input():
    content = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    return (item for item in content.split('\n\n'))


def get_answer(input):
    valid = 0
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for item in input:
        keys = {match.group('key') for match in rx_key_value.finditer(item)}
        print(keys)
        valid += 0 if required - keys else 1

    return valid


if __name__ == '__main__':
    t0 = time()
    print(f'answer: {get_answer(get_input())}')
    print(f'{time() - t0}')

