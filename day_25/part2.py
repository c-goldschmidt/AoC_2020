from utils import run


def get_input(content):
    return [line for line in content.split('\n') if line]


def get_answer(_):
    return "Merry X-Mas"


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
