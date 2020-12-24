import copy

from day_24.part1 import TileGrid, get_input
from utils import run


class ConwaysTileGrid(TileGrid):

    def __init__(self):
        super().__init__()

    def get_neighbors(self, coords):
        neighbors = []
        for direction in self.directions.values():
            neighbors.append((
                coords[0] + direction[0],
                coords[1] + direction[1],
                coords[2] + direction[2],
            ))
        return neighbors

    def __getitem__(self, directions):
        if isinstance(directions, str):
            return super().__getitem__(directions)

        return self.tiles[directions]

    def __setitem__(self, directions, value):
        if isinstance(directions, str):
            super().__setitem__(directions, value)
        else:
            self.tiles[directions] = value

    def fill(self):
        for coords, tile in list(self.tiles.items()):
            for neigh in self.get_neighbors(coords):
                _ = self[neigh]  # fetch value from defaultdict, creating tiles not existing yet

    def tick(self):
        self.fill()
        next_grid = ConwaysTileGrid()

        # pre-fetch currently exiting tiles before they are altered
        for coords, tile in list(self.tiles.items()):
            alive = 0
            for neigh in self.get_neighbors(coords):
                alive += 1 if self[neigh] else 0

            if tile and (alive == 0 or alive > 2):
                next_grid[coords] = False
            elif not tile and alive == 2:
                next_grid[coords] = True
            else:
                next_grid[coords] = tile

        return next_grid


def get_answer(input):
    grid = ConwaysTileGrid()

    for directions in input:
        grid[directions] = not grid[directions]

    for i in range(100):
        grid = grid.tick()

    return grid.count()


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
