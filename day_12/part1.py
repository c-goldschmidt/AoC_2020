import re

from utils import run

rx_data = re.compile(r'^(?P<direction>\w)(?P<value>\d+)$', re.MULTILINE)
DIRECTIONS = ['N', 'E', 'S', 'W']


def get_input(content):
    return rx_data.finditer(content)


def next_facing(direction, value, current_facing):
    index = current_facing

    if direction == 'L':
        index = int((current_facing - (value / 90)) % len(DIRECTIONS))

    if direction == 'R':
        index = int((current_facing + (value / 90)) % len(DIRECTIONS))

    return index


def move(direction, value, current_position):
    if direction == 'N':
        current_position[0] += value
    if direction == 'E':
        current_position[1] += value
    if direction == 'S':
        current_position[0] -= value
    if direction == 'W':
        current_position[1] -= value
    return current_position


def next_position(direction, value, current_facing, current_position):
    if direction == 'F':
        return move(DIRECTIONS[current_facing], value, current_position)

    if direction in DIRECTIONS:
        return move(direction, value, current_position)

    return current_position


def get_answer(input):
    current_position = [0, 0]
    current_facing = 1

    for match in input:
        direction = match.group('direction')
        value = int(match.group('value'))
        current_facing = next_facing(direction, value, current_facing)
        current_position = next_position(direction, value, current_facing, current_position)

    return sum([abs(current_position[0]), abs(current_position[1])])


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
