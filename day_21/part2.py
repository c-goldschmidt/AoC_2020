import copy
from collections import defaultdict

from day_21.part1 import get_possible_allergens, get_input, rx_content
from utils import run


def test_foods(foods, replacements):
    for item in foods:
        line_replaced = [replacements[item] if item in replacements else item for item in item[0]]

        missing_allergens = item[1] - set(line_replaced)
        if missing_allergens:
            return False
    return True


def get_foods(input):
    foods = []
    for line in input:
        content = rx_content.search(line)
        ingredients = set(content.group('ingredients').split(' '))
        allergens = set(content.group('allergens').split(', '))
        foods.append((ingredients, allergens))
    return foods


def iterate_dict_list(replacements):
    for key, values in replacements.items():
        clone = copy.deepcopy(replacements)
        del clone[key]

        if not clone:
            for value in values:
                yield {key: value}

        for sub in iterate_dict_list(clone):
            for value in values:
                if value is not None:
                    yield {key: value, **sub}
                else:
                    yield sub


def get_allergen_mapping(foods, possible_allergens):
    replacements = defaultdict(set)
    for allergen, ingredients in possible_allergens.items():
        for ingredient in ingredients:
            replacements[ingredient].add(allergen)
            replacements[ingredient].add(None)

    for combination in iterate_dict_list(replacements):
        if test_foods(foods, combination):
            return combination


def get_answer(input):
    foods = get_foods(input)
    possible_allergens, _ = get_possible_allergens(input)
    mapping = get_allergen_mapping(foods, possible_allergens)

    result = [key for key, value in sorted(mapping.items(), key=lambda x:x[1])]
    return ','.join(result)


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
