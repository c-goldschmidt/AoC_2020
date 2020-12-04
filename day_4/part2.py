import os
import re
from time import time

from utils import read_file

rx_key_value = re.compile(r'(?P<key>\w{3}):(?P<value>\S+)(\s|$)')
rx_size = re.compile(r'^(?P<num>\d+)(?P<unit>\w{2})$')
rx_color = re.compile(r'^#[a-f0-9]{6}$')
rx_pid = re.compile(r'^\d{9}$')


def get_input():
    content = read_file(os.path.join(os.path.dirname(__file__), 'input.txt'))
    return (item for item in content.split('\n\n'))


def validate(key, value):
    value = value.strip()

    if key == 'byr':
        return 1920 <= int(value) <= 2002
    if key == 'iyr':
        return 2010 <= int(value) <= 2020
    if key == 'eyr':
        return 2020 <= int(value) <= 2030
    if key == 'hgt':
        match = rx_size.search(value)
        if not match:
            return False

        value = int(match.group('num'))
        if match.group('unit') == 'cm':
            return 150 <= value <= 193
        return 59 <= value <= 76
    if key == 'hcl':
        return rx_color.match(value)
    if key == 'ecl':
        return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    if key == 'pid':
        return rx_pid.match(value)
    return True


def is_item_valid(item):
    for match in rx_key_value.finditer(item):
        key = match.group('key')
        value = match.group('value')

        if not validate(key, value):
            return False
    return True


def get_answer(input):
    num_valid = 0
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for item in input:
        keys = {match.group('key') for match in rx_key_value.finditer(item)}
        if required - keys:
            continue

        num_valid += int(is_item_valid(item))
    return num_valid


if __name__ == '__main__':
    t0 = time()
    print(f'answer: {get_answer(get_input())}')
    print(f'{time() - t0}')

