import re

from utils import run

rx_parenthesis = re.compile(r'\((?P<expression>[0-9 *+]+)\)')
rx_calc = re.compile(r'\d+ [+*] \d+')


def get_input(content):
    return [line for line in content.split('\n') if line]


def wrong_math(line):
    def replace_equation(match):
        return wrong_math(match.group('expression'))

    line = rx_parenthesis.sub(replace_equation, line)

    def replace_calc(match):
        return f'{eval(match.group(0))}'

    line = rx_calc.sub(replace_calc, line, 1)
    if rx_parenthesis.search(line) or rx_calc.search(line):
        return wrong_math(line)

    return line


def get_answer(input):
    total = 0
    for line in input:
        total += int(wrong_math(line))
    return total


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
