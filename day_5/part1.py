import re

from utils import run

rx_data = re.compile(r'^(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<pass>\w+)$', re.MULTILINE)


def get_input(content):
    return (row for row in content.split('\n') if row)


def get_seat(arr, letter):
    half = len(arr) // 2
    if letter in ('F', 'L'):
        return arr[:half]
    return arr[half:]


def get_answer(input):
    seat_ids = []
    for keys in input:
        rows = list(range(128))

        for key in keys[:7]:
            rows = get_seat(rows, key)

        columns = list(range(8))
        for key in keys[7:]:
            columns = get_seat(columns, key)

        seat_ids.append(rows[0] * 8 + columns[0])

    return max(*seat_ids)


if __name__ == '__main__':
    run(__file__, get_input, get_answer)

