import itertools
import math
import pprint
import re
from time import time

from utils import run

rx_tile_id = re.compile(r'Tile (?P<num>\d+):')

pp = pprint.PrettyPrinter(indent=4)


class Border:
    EXISTING = {}

    @classmethod
    def create(cls, border):
        if isinstance(border, Border):
            return border

        hashed = hash(''.join(border))
        if hashed not in cls.EXISTING:
            cls.EXISTING[hashed] = Border(border, hashed)
        return cls.EXISTING[hashed]

    def __init__(self, border, hash):
        self.list = border
        self.content = ''.join(self.list)
        self.hash = hash

    def reverse(self):
        return Border.create(list(reversed(self.list)))

    def __eq__(self, other):
        return hash(other) == self.hash

    def __str__(self):
        return self.content

    def __repr__(self):
        return self.content

    def __hash__(self):
        return self.hash


class Borders:
    EXISTING = {}

    @classmethod
    def create(cls, borders):
        borders = [Border.create(border) for border in borders]
        hashed = hash('/'.join([str(hash(border)) for border in borders]))
        if hashed not in cls.EXISTING:
            cls.EXISTING[hashed] = Borders(borders, hashed)
            cls.EXISTING[hashed].update_perms()
        return cls.EXISTING[hashed]

    def __init__(self, borders, hashed):
        self._borders = borders
        self._hash = hashed
        self.permutations = None

    def __str__(self):
        return ','.join([str(border) for border in self._borders])

    def __repr__(self):
        return str(self)

    def update_perms(self):
        self.permutations = self.get_border_permutations()

    def get_permutation(self, key):
        return self.permutations[key]

    def get_border_permutations(self):
        direct = {
            'horizontal-flip': self._flip_horizontal(),
            'vertical-flip': self._flip_vertical(),
            'rotate-90': self._rotate(1),
            'rotate-180': self._rotate(2),
            'rotate-270': self._rotate(3),
        }

        found = {hash(self)}
        all_perms = {**direct}
        for key, value in direct.items():
            if hash(value) in found:
                continue

            if not value.permutations:
                continue

            found.add(value)
            for sub_key, sub_value in value.permutations.items():
                if hash(sub_value) in found:
                    continue
                found.add(hash(sub_value))
                all_perms[f'{key}_{sub_key}'] = sub_value

        return {
            'default': self,
            **all_perms,
        }

    def _flip_horizontal(self):
        return Borders.create([
            self._borders[0].reverse(),
            self._borders[3],
            self._borders[2].reverse(),
            self._borders[1],
        ])

    def _flip_vertical(self):
        return Borders.create([
            self._borders[2],
            self._borders[1].reverse(),
            self._borders[0],
            self._borders[3].reverse(),
        ])

    def _rotate(self, steps):
        curr = self._borders
        for _i in range(steps):
            curr = [
                curr[1],
                curr[2].reverse(),
                curr[3],
                curr[0].reverse(),
            ]
        return Borders.create(curr)

    def __getitem__(self, item):
        return self._borders[item]

    def __hash__(self):
        return self._hash


class Tile:
    def __init__(self, content):
        lines = [line for line in content.split('\n') if line]
        self.id = int(rx_tile_id.search(lines[0]).group('num'))
        self.image_data = lines[1:]

        self.orientation = 'default'
        self._borders = Borders.create([
            [dot for dot in self.image_data[0]],
            [line[-1] for line in self.image_data],
            [dot for dot in self.image_data[-1]],
            [line[0] for line in self.image_data],
        ])

    def fit_right_of(self, other):
        for key, border in self._borders.permutations.items():
            if other.oriented_borders[1] == border[3]:
                return key
        return None

    def fit_bottom_of(self, other):
        for key, border in self._borders.permutations.items():
            if other.oriented_borders[2] == border[0]:
                return key
        return None

    @property
    def oriented_borders(self):
        return self._borders.get_permutation(self.orientation)

    @property
    def border_permutations(self):
        return self._borders.permutations

    def __hash__(self):
        return self.id

    def __str__(self):
        return f'Tile {self.id}'

    def __repr__(self):
        return f'Tile {self.id}'


class OrientedTile:
    def __init__(self, tile, orientation):
        self.tile = tile
        self.orientation = orientation

    def fit_right_of(self, other):
        other.tile.orientation = other.orientation
        self.tile.orientation = self.orientation
        if other.tile.oriented_borders[1] == self.tile.oriented_borders[3]:
            return True
        return False

    def fit_bottom_of(self, other):
        other.tile.orientation = other.orientation
        self.tile.orientation = self.orientation
        if other.tile.oriented_borders[2] == self.tile.oriented_borders[0]:
            return True
        return False

    def __eq__(self, other):
        return self.tile.id == other.tile.id and self.orientation == other.orientation

    def __hash__(self):
        return self.tile.id

    def __repr__(self):
        return f'OrientedTile {self.tile} @ {self.orientation}'


class Chain(list):
    def __init__(self, from_list):
        super().__init__(from_list)
        self.hashes = [hash(item) for item in from_list]
        self.hash = hash(','.join([str(i) for i in self.hashes]))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        for i, item in enumerate(other):
            if self[i] != item:
                return False
        return True

    def __contains__(self, obj):
        return hash(obj) in self.hashes


def get_input(content):
    return [Tile(tile) for tile in content.split('\n\n') if tile]


def find_lines(input, length):
    all_pairs = find_pairs(input)
    chains = all_pairs
    curr_len = 2
    while curr_len < length:
        new_chains = set()

        for chain in chains:
            for pair in all_pairs:
                if pair[1] not in chain and pair[0] == chain[-1]:
                    new_chains.add(Chain([*chain, pair[1]]))
                elif pair[0] not in chain and pair[1] == chain[0]:
                    new_chains.add(Chain([pair[0], *chain]))

        chains = new_chains
        curr_len += 1

    return chains


def find_pairs(input):
    pairs = []
    for perm in itertools.permutations(input, 2):
        for key in perm[0].border_permutations:
            perm[0].orientation = key
            orientation = perm[1].fit_right_of(perm[0])
            if orientation:
                pairs.append(Chain([OrientedTile(perm[0], key), OrientedTile(perm[1], orientation)]))
    return pairs


def find_line_pairs(lines):
    pairs = []
    for perm in itertools.permutations(lines, 2):
        if len(set(perm[0]) & set(perm[1])) > 0:
            continue

        fits = True
        for i, item in enumerate(perm[0]):
            if not perm[1][i].fit_bottom_of(item):
                fits = False
                break

        if fits:
            pairs.append(Chain([perm[0], perm[1]]))

    return pairs


def pic_valid(chain):
    used_ids = [hash(item) for line in chain for item in line]
    return len(set(used_ids)) == len(used_ids)


def find_image(input, length, return_first=True):
    lines = find_lines(input, length)
    print('found lines: ', len(lines))
    line_pairs = find_line_pairs(lines)

    chains = set(line_pairs)
    curr_len = 2
    while curr_len < length:
        new_chains = set()

        for chain in chains:
            for pair in line_pairs:
                new_chain = None
                if pair[1] not in chain and pair[0] == chain[-1]:
                    new_chain = Chain([*chain, pair[1]])
                elif pair[0] not in chain and pair[1] == chain[0]:
                    new_chain = Chain([pair[0], *chain])

                if new_chain and pic_valid(new_chain):
                    if len(new_chain) == length and return_first:
                        return new_chain
                    new_chains.add(new_chain)

        chains = new_chains
        curr_len += 1

    return chains


def get_answer(input):
    size = int(math.sqrt(len(input)))
    image = find_image(input, size)

    return math.prod([
        image[0][0].tile.id,
        image[0][-1].tile.id,
        image[-1][0].tile.id,
        image[-1][-1].tile.id,
    ])


if __name__ == '__main__':
    run(__file__, get_input, get_answer)

