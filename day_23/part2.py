from day_23.part1 import get_input, Cup, move, run_for_moves
from utils import run


def create_circle(input):
    current = input.prev

    for i in range(10, 1_000_000 + 1):
        cup = Cup(i)
        cup.prev = current
        current.next = cup
        current = cup

    current.next = input
    input.prev = current


def get_answer(input):
    create_circle(input)

    cup_1 = run_for_moves(input, 10_000_000)
    return cup_1.next.value * cup_1.next.next.value


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
