import re

from utils import run

rx_data = re.compile(r'^(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<pass>\w+)$', re.MULTILINE)


def get_input(content):
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
    run(__file__, get_input, get_answer)

