import re

from utils import run

rx_data = re.compile(r'^(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<pass>\w+)$', re.MULTILINE)


def get_input(content):
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
    run(__file__, get_input, get_answer)

