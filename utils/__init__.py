import importlib.util
import os
from time import time


def read_file(file_name: str):
    with open(file_name, 'r') as f:
        return f.read()


def run(filename, get_input, get_answer):
    content = read_file(os.path.join(os.path.dirname(filename), 'input.txt'))

    t0 = time()
    print(f'answer: {get_answer(get_input(content))}')
    print(f'{time() - t0}')


def run_day(day_num: int):
    day = f'day_{day_num}'
    dirname = os.path.join(os.path.dirname(__file__), '..', day)

    for part in ('part1', 'part2'):
        mod = importlib.import_module(f'{day}.{part}')
        filename = os.path.join(dirname, f'{part}.py')
        run(filename, mod.get_input, mod.get_answer)
