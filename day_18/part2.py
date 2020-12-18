import re

from day_18.part1 import rx_parenthesis, get_input
from utils import run

rx_add = re.compile(r'\d+ \+ \d+')
rx_mul = re.compile(r'\d+ \* \d+')


def wrong_math(line):
    def replace_equation(match):
        return wrong_math(match.group('expression'))

    line = rx_parenthesis.sub(replace_equation, line)

    def replace_calc(match):
        return f'{eval(match.group(0))}'

    line = rx_add.sub(replace_calc, line)
    if rx_parenthesis.search(line) or rx_add.search(line):
        return wrong_math(line)

    line = rx_mul.sub(replace_calc, line)
    if rx_mul.search(line):
        return wrong_math(line)

    return line


def get_answer(input):
    total = 0
    for line in input:
        total += int(wrong_math(line))
    return total


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
