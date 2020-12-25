import math

from day_13.part2 import inverse_mod
from utils import run


def get_input(content):
    lines = content.split('\n')
    return int(lines[0]), int(lines[1])


def transform_subject(loop_size, subject):
    result = 1
    for i in range(loop_size):
        result = (result * subject) % 20201227
    return result


def get_loop_size(key):
    value = 1
    loop_size = 0
    while value != key:
        loop_size += 1
        value = value * 7 % 20201227

    return loop_size


def get_answer(input):
    card, door = input[0], input[1]
    card_loop = get_loop_size(card)
    return transform_subject(card_loop, door)


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
