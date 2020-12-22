import copy
import math

from day_20.part1 import find_image, get_input, OrientedTile, Tile
from utils import run


def remove_borders(tile: OrientedTile):
    return [list(line)[1:-1] for line in tile.tile.image_data[1:-1]]


def rotate(image_data, steps):
    img_len = len(image_data)

    for _i in range(steps):
        result = copy.deepcopy(image_data)

        for y in range(img_len):
            for x in range(img_len):
                x_new, y_new = y, (img_len - 1) - x
                result[y_new][x_new] = image_data[y][x]
        image_data = result

    return image_data


def apply_transform(tile, clean_borders=True):
    if clean_borders:
        image_data = remove_borders(tile)
    else:
        image_data = copy.deepcopy([list(line) for line in tile.tile.image_data])

    for transform in tile.orientation.split('_'):
        if transform == 'vertical-flip':
            image_data.reverse()
        if transform == 'horizontal-flip':
            image_data = [list(reversed(line)) for line in image_data]
        if transform == 'rotate-90':
            image_data = rotate(image_data, 1)
        if transform == 'rotate-180':
            image_data = rotate(image_data, 2)
        if transform == 'rotate-270':
            image_data = rotate(image_data, 3)

    return image_data


def replace_monsters(image_data):
    img_size = len(image_data)
    monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   ',
    ]

    monster_found = False
    for y in range(0, img_size - 3):
        for x in range(0, img_size - 20):
            monster_fits = True
            monster_replaced = copy.deepcopy(image_data)
            for y2, line_data in enumerate(monster):
                for x2, chr in enumerate(line_data):
                    if chr == ' ':
                        continue

                    if image_data[y + y2][x + x2] != '#':
                        monster_fits = False
                        break
                    monster_replaced[y + y2][x + x2] = 'O'

                if not monster_fits:
                    break

            if monster_fits:
                monster_found = True
                image_data = monster_replaced

    return monster_found, image_data


def extract_sea_monsters2(image):
    image_data = []

    for i, line in enumerate(image):
        for tile in line:
            img = apply_transform(tile)
            x = len(img)
            for j, img_line in enumerate(img):
                line_offset = i * x + j
                if line_offset >= len(image_data):
                    image_data.append([])
                image_data[line_offset] += img_line

    monster_tile = Tile('Tile 666:\n' + '\n'.join([''.join(line) for line in image_data]))
    for orientation in monster_tile.border_permutations:
        print('try', orientation)
        image_data = apply_transform(OrientedTile(monster_tile, orientation), False)
        found, data = replace_monsters(image_data)
        if found:
            # print('\n'.join([''.join(line) for line in data]))
            return count_roughness(data)
    return None


def extract_sea_monsters(image):
    image_data = []

    for i, line in enumerate(image):
        for tile in line:
            img = apply_transform(tile)
            x = len(img)
            for j, img_line in enumerate(img):
                line_offset = i * x + j
                if line_offset >= len(image_data):
                    image_data.append([])
                image_data[line_offset] += img_line

    found, data = replace_monsters(image_data)
    if found:
        return count_roughness(data)
    return None


def count_roughness(image):
    result = 0
    for line in image:
        result += len([x for x in line if x == '#'])
    return result


def get_answer(input):
    size = int(math.sqrt(len(input)))
    image = find_image(input, size)
    return extract_sea_monsters2(image)


if __name__ == '__main__':
    run(__file__, get_input, get_answer)

