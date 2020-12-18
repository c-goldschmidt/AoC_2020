import copy
from utils import run


class Cube:
    def __init__(self, x, y, z, w, active):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.active = active
        self.neighbors = 0

    def find_neighbors(self, cubes, fourth_dimension=False):
        neighbors = 0
        for x in range(self.x - 1, self.x + 2):
            for y in range(self.y - 1, self.y + 2):
                for z in range(self.z - 1, self.z + 2):
                    w_range = range(0, 1)
                    if fourth_dimension:
                        w_range = range(self.w - 1, self.w + 2)

                    for w in w_range:
                        if x == self.x and y == self.y and z == self.z and w == self.w:
                            continue

                        cube = new_cube(cubes, x, y, z, w)
                        if cube.active:
                            neighbors += 1
        self.neighbors = neighbors

    def tick(self):
        if self.active and self.neighbors not in [2, 3]:
            self.active = False
        if (not self.active) and self.neighbors == 3:
            self.active = True

    def __str__(self):
        return f"{','.join([self.x, self.y, self.z, self.w])} - {self.active}"

    def __repr__(self):
        return f"{self.active}"


def get_input(content):
    return [line for line in content.split('\n') if line]


def cube_at(cubes, x, y, z, w):
    if f"{x},{y},{z},{w}" in cubes.keys():
        return cubes[f"{x},{y},{z},{w}"]
    return None


def new_cube(cubes, x, y, z, w, default=False):
    cube = cube_at(cubes, x, y, z, w)
    if not cube:
        cube = Cube(x, y, z, w, default)
        cubes[f"{x},{y},{z},{w}"] = cube
    return cube


def boot_cubes(data, fourth_dimension=False):
    cubes = {}
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == "#":
                new_cube(cubes, x, y, 0, 0, True)

    for pos, cube in list(cubes.items()):
        cube.find_neighbors(cubes, fourth_dimension)

    return cubes


def run_for_input(input, fourth_dimension=False):
    cubes = boot_cubes(input, fourth_dimension)

    for i in range(6):
        for pos, cube in list(cubes.items()):
            cube.find_neighbors(cubes, fourth_dimension)

        next_cubes = copy.deepcopy(cubes)

        for pos, sub_cube in next_cubes.items():
            sub_cube.tick()
            cube = cube_at(cubes, sub_cube.x, sub_cube.y, sub_cube.z, sub_cube.w)
            cube.active = sub_cube.active
    return cubes


def get_answer(input):
    cubes = run_for_input(input)

    n = 0
    for pos, cube in cubes.items():
        if cube.active:
            n += 1
    return n


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
