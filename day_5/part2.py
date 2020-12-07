import itertools
import re

from day_5.part1 import get_seat
from utils import run

rx_data = re.compile(r'^(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<pass>\w+)$', re.MULTILINE)


def get_input(content):
    return (row for row in content.split('\n') if row)


def get_answer(input):
    hits = set()
    hit_rows = []
    for keys in input:
        rows = list(range(128))

        for key in keys[:7]:
            rows = get_seat(rows, key)

        columns = list(range(8))
        for key in keys[7:]:
            columns = get_seat(columns, key)

        hits.add((rows[0], columns[0]))
        hit_rows.append(rows[0])

    min_row = min(*hit_rows)
    max_row = max(*hit_rows)
    all_seats = set(itertools.product(range(min_row + 1, max_row), range(8)))
    missing = list(all_seats - hits)
    return missing[0][0] * 8 + missing[0][1]


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
