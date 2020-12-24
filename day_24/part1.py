import re
from collections import defaultdict

from utils import run

rx_tiles = re.compile('(?P<item>se|sw|ne|nw|w|e)')


class TileGrid:
    directions = {
        'e': (1, -1, 0),
        'w': (-1, 1, 0),
        'ne': (1, 0, -1),
        'nw': (0, 1, -1),
        'se': (0, -1, 1),
        'sw': (-1, 0, +1),
    }

    def __init__(self):
        self.tiles = defaultdict(lambda: False)

    def count(self):
        count = 0
        for tile in self.tiles.values():
            count += 1 if tile else 0
        return count

    def __getitem__(self, directions):
        return self.tiles[self._to_location(directions)]

    def __setitem__(self, directions, value):
        self.tiles[self._to_location(directions)] = value

    def _to_location(self, directions):
        location = [0, 0, 0]
        for direction in rx_tiles.finditer(directions):
            location[0] += self.directions[direction.group('item')][0]
            location[1] += self.directions[direction.group('item')][1]
            location[2] += self.directions[direction.group('item')][2]

        return tuple(location)


def get_input(content):
    return [line for line in content.split('\n') if line]


def get_answer(input):
    grid = TileGrid()

    for directions in input:
        grid[directions] = not grid[directions]

    return grid.count()


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
