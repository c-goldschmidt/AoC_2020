import re
from collections import defaultdict
from utils import run

rx_content = re.compile(r'^(?P<ingredients>.+?) \(contains (?P<allergens>.+?)\)$')


def get_input(content):
    return [line for line in content.split('\n') if line]


def get_possible_allergens(input):
    possible_allergens = defaultdict(set)
    ingredients_dict = defaultdict(int)
    for line in input:
        content = rx_content.search(line)
        ingredients = set(content.group('ingredients').split(' '))
        for ingredient in ingredients:
            ingredients_dict[ingredient] += 1

        for allergen in content.group('allergens').split(', '):
            if len(possible_allergens[allergen]) == 0:
                possible_allergens[allergen] = ingredients
            possible_allergens[allergen] = possible_allergens[allergen] & ingredients

    return possible_allergens, ingredients_dict


def get_answer(input):
    possible_allergens, ingredients_dict = get_possible_allergens(input)

    all_ingredients = set(ingredients_dict.keys())
    with_allergens = set()
    for value in possible_allergens.values():
        with_allergens |= value

    total = 0
    for item in all_ingredients - with_allergens:
        total += ingredients_dict[item]
    return total


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
