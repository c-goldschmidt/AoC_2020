import re

from utils import run

rx_classes = re.compile(r'^(?P<class>.+): (?P<low_start>\d+)-(?P<low_end>\d+) or (?P<high_start>\d+)-(?P<high_end>\d+)$')

class Class:
    def __init__(self, match):
        self.name = match.group('class')
        self.low_start = int(match.group('low_start'))
        self.low_end = int(match.group('low_end'))
        self.high_start = int(match.group('high_start'))
        self.high_end = int(match.group('high_end'))

    def fits(self, num):
        return self.low_start <= num <= self.low_end or self.high_start <= num <= self.high_end


def get_input(content):
    split = content.split('\n\n')

    def as_numbers(input):
        return [int(value) for value in input.split(',') if value]

    return (
        split[0].split('\n'),
        as_numbers(split[1].split('\n')[1]),
        [as_numbers(line) for line in split[2].split('\n')[1:] if line],
    )


def get_classes(input):
    return [Class(rx_classes.match(line)) for line in input[0]]


def get_answer(input):
    classes = get_classes(input)
    errors = []
    for other in input[2]:
        for value in other:
            has_fitting = False
            for klass in classes:
                if klass.fits(value):
                    has_fitting = True
            if not has_fitting:
                errors.append(value)

    return sum(errors)


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
