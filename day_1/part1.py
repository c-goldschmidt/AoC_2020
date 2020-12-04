import itertools

from utils import run


def get_input(content):
    return [item for item in content.split('\n') if item]


def get_answer(input):
    input.sort(reverse=True)
    for x, y in itertools.product(input, input):
        x = int(x)
        y = int(y)

        if x + y == 2020:
            return x * y


if __name__ == '__main__':
    run(__file__, get_input, get_answer)

