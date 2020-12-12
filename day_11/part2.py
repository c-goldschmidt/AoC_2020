from day_11.part1 import get_input, Grid
from utils import run


class VisionGrid(Grid):

    def view_direction(self, x, y, dx, dy):
        y += dy
        x += dx

        while 0 <= x < len(self.grid) and 0 <= y < len(self.grid[x]):
            #print("check", x, y)
            if self.grid[x][y].is_seat:
                #print("=>", 1 if self.grid[x][y].is_occupied else 0)
                return 1 if self.grid[x][y].is_occupied else 0

            y += dy
            x += dx
        return 0

    def count_neighbors(self, x, y):
        count = 0
        count += self.view_direction(x, y, 0, 1)
        count += self.view_direction(x, y, 0, -1)
        count += self.view_direction(x, y, 1, 0)
        count += self.view_direction(x, y, 1, 1)
        count += self.view_direction(x, y, 1, -1)
        count += self.view_direction(x, y, -1, 0)
        count += self.view_direction(x, y, -1, 1)
        count += self.view_direction(x, y, -1, -1)
        return count


def get_answer(input):
    grid = VisionGrid(input, 5)
    return grid.run()


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
