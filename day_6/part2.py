from utils import run


def get_input(content):
    return (row for row in content.split('\n\n') if row)


def get_answer(input):
    total = 0
    for group in input:
        group_answers = None

        for answer in group.split('\n'):
            if group_answers is None:
                group_answers = set(answer)
            else:
                group_answers = group_answers & set(answer)

        total += len(group_answers)
    return total


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
