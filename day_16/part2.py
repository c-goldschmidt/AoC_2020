from collections import defaultdict

from day_16.part1 import get_classes, get_input
from utils import run


def filter_tickets(classes, others):
    filtered = []
    for other in others:
        has_fitting = False
        for value in other:
            has_fitting = False
            for klass in classes:
                if klass.fits(value):
                    has_fitting = True

            if not has_fitting:
                break

        if has_fitting:
            filtered.append(other)
    return filtered


def get_answer(input):
    classes = get_classes(input)
    classes_by_index = defaultdict(set)
    filtered = filter_tickets(classes, input[2])

    for ticket in filtered:
        for index, value in enumerate(ticket):
            for klass in classes:
                if klass.fits(value):
                    classes_by_index[index].add(klass)

    for ticket in filtered:
        for index, value in enumerate(ticket):
            remove = set()
            for klass in classes_by_index[index]:
                if not klass.fits(value):
                    remove.add(klass)

            classes_by_index[index] -= remove

    in_order = [None for _ in classes_by_index.keys() ]
    for _ in range(len(classes_by_index.keys())):
        for i, items in classes_by_index.items():
            if len(items) == 1:
                removed = list(items)[0]
                in_order[i] = removed

                for j, items in classes_by_index.items():
                    classes_by_index[j] -= {removed}

    result = 1
    for i, klass in enumerate(in_order):
        if klass.name.startswith('departure'):
            result *= input[1][i]

    return result


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
