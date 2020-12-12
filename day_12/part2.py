import math

from day_12.part1 import get_input, DIRECTIONS, move
from utils import run


def move_to_waypoint(times, waypoint_pos, ship_pos):
    delta_pos = [
        waypoint_pos[0] - ship_pos[0],
        waypoint_pos[1] - ship_pos[1],
    ]
    for _i in range(times):
        waypoint_pos[0] += delta_pos[0]
        waypoint_pos[1] += delta_pos[1]
        ship_pos[0] += delta_pos[0]
        ship_pos[1] += delta_pos[1]


def rotate_waypoint(direction, value, ship_pos, waypoint_pos):
    delta_pos = [
        waypoint_pos[0] - ship_pos[0],
        waypoint_pos[1] - ship_pos[1],
    ]

    for i in range(int(value / 90)):
        if direction == 'R':
            delta_pos = [
                delta_pos[1] * -1,
                delta_pos[0],
            ]
        else:
            delta_pos = [
                delta_pos[1],
                delta_pos[0] * -1,
            ]

    waypoint_pos[0] = ship_pos[0] + delta_pos[0]
    waypoint_pos[1] = ship_pos[1] + delta_pos[1]


def get_answer(input):
    ship_position = [0, 0]
    waypoint_position = [1, 10]

    for match in input:
        direction = match.group('direction')
        value = int(match.group('value'))

        if direction in ('R', 'L'):
            rotate_waypoint(direction, value, ship_position, waypoint_position)

        if direction in DIRECTIONS:
            move(direction, value, waypoint_position)

        if direction == 'F':
            move_to_waypoint(value, waypoint_position, ship_position)

    return sum([abs(ship_position[0]), abs(ship_position[1])])


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
