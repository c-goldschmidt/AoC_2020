import copy

from utils import run


class GridItem:
    def __init__(self, is_seat):
        self.is_seat = is_seat
        self.is_occupied = False

    def __copy__(self):
        copied = GridItem(self.is_seat)
        copied.is_occupied = self.is_occupied
        return copied

    def __deepcopy__(self, *args):
        return self.__copy__()

    def __eq__(self, other):
        return other.is_seat == self.is_seat and other.is_occupied == self.is_occupied

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '#' if self.is_occupied else 'L' if self.is_seat else '.'


def get_input(content):
    grid = []
    for row in content.split('\n'):
        if not row:
            continue
        grid_row = []
        for column in row:
            grid_row.append(GridItem(column == 'L'))
        grid.append(grid_row)

    return grid


class Grid:
    def __init__(self, grid, seat_limit = 4):
        self.grid = grid
        self.seat_limit = seat_limit

    def run(self):
        stable = False
        while not stable:
            next = self.iterate()
            stable = self.compare(next, self.grid)
            # print(next)
            self.grid = next

        return self.count()

    def count_neighbors(self, x, y):
        occupied = 0
        for cx in range(x - 1, x + 2):
            if cx < 0 or cx > len(self.grid) - 1:
                continue

            for cy in range(y - 1, y + 2):
                if cy < 0 or cy > len(self.grid[cx]) - 1 or (cx == x and cy == y):
                    continue

                occupied += 1 if self.grid[cx][cy].is_occupied else 0
        return occupied

    def iterate(self):
        new_grid = copy.deepcopy(self.grid)

        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if not self.grid[x][y].is_seat:
                    continue

                neighbors = self.count_neighbors(x, y)
                if self.grid[x][y].is_occupied and neighbors >= self.seat_limit:
                    new_grid[x][y].is_occupied = False
                if not self.grid[x][y].is_occupied and neighbors == 0:
                    new_grid[x][y].is_occupied = True

        return new_grid

    @staticmethod
    def compare(grid_a, grid_b):
        for x in range(len(grid_a)):
            for y in range(len(grid_a[x])):
                if grid_a[x][y] != grid_b[x][y]:
                    return False
        return True

    def count(self):
        seats = 0
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y].is_seat and self.grid[x][y].is_occupied:
                    seats += 1
        return seats


def get_answer(input):
    grid = Grid(input)
    return grid.run()


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
