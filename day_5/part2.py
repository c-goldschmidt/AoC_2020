from utils import run


def get_input(content):
    return (item for item in content.split('\n'))


def get_answer(input):
    return 0


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
