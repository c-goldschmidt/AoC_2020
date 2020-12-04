from utils import run


def get_input(content):
    return content.split('\n')


def get_answer(input):
    x = 3
    count = 0
    for line in input[1:]:
        if not len(line):
            continue
        count += 1 if line[x % len(line)] == '#' else 0
        x += 3

    return count


if __name__ == '__main__':
    run(__file__, get_input, get_answer)

