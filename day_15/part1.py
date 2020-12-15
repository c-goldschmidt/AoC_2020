from utils import run


def get_input(content):
    return [int(num) for num in content.split('\n')[0].split(',')]


def run_to_iteration(input, turns):
    memory = {}
    for i, starter in enumerate(input):
        memory[starter] = [i + 1, i + 1]

    prev = input[-1]
    for turn in range(len(input) + 1, turns + 1):
        if prev in memory:
            value = memory[prev][1] - memory[prev][0]
        else:
            value = 0
        prev = value

        memory[prev] = [
            memory[prev][1] if prev in memory else turn,
            turn,
        ]

    return prev


def get_answer(input):
    return run_to_iteration(input, 2020)


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
