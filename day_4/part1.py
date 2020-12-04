import re

from utils import run

rx_key_value = re.compile(r'(?P<key>\w{3})')


def get_input(content):
    return (item for item in content.split('\n\n'))


def get_answer(input):
    valid = 0
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for item in input:
        keys = {match.group('key') for match in rx_key_value.finditer(item)}
        valid += 0 if required - keys else 1

    return valid


if __name__ == '__main__':
    run(__file__, get_input, get_answer)

