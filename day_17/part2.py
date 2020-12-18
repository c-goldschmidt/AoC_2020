from day_17.part1 import run_for_input, get_input
from utils import run


def get_answer(input):
    cubes = run_for_input(input, True)

    n = 0
    for pos, cube in cubes.items():
        if cube.active:
            n += 1
    return n


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
