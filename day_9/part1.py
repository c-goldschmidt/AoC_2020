import itertools

from utils import run


def get_input(content):
    return [int(row) for row in content.split('\n') if row]


def is_valid(item, input):
    for i, j in itertools.product(input, input):
        if i == j:
            continue
        if i + j == item:
            return True
    return False


def get_answer(input):
    for i, row in enumerate(input[25:]):
        if not is_valid(row, input[i:i + 25]):
            return row
    return 0


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
