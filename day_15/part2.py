from utils import run

from day_15.part1 import run_to_iteration, get_input


def get_answer(input):
    # there's probably a math way to do this, but meh...
    return run_to_iteration(input, 30000000)


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
