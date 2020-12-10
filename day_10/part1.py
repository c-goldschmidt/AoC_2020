from utils import run


def get_input(content):
    return [int(row) for row in content.split('\n') if row]


def get_answer(input):
    input.sort()

    diff_1 = 0
    diff_3 = 1  # add one for device itself

    for i, value in enumerate(input):
        prev = input[i - 1] if i > 0 else 0
        diff = value - prev
        diff_1 += 1 if diff == 1 else 0
        diff_3 += 1 if diff == 3 else 0

    return diff_1 * diff_3


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
