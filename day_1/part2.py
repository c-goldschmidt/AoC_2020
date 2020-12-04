import itertools

from utils import run


def get_input(content):
    return [item for item in content.split('\n') if item]


def get_answer(input):
    input.sort(reverse=True)
    for [x, y], z in itertools.product(itertools.product(input, input), input):
        x = int(x)
        y = int(y)
        z = int(z)
        if x + y + z == 2020:
            return x * y * z


if __name__ == '__main__':
    run(__file__, get_input, get_answer)

