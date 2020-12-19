from day_19.part1 import create_rules_dict, count_matches, get_input, Rule
from utils import run


def get_answer(input):
    rules_dict = create_rules_dict(input[0])

    rules_dict['8'] = Rule('42 | 42 8', rules_dict)
    rules_dict['11'] = Rule('42 31 | 42 11 31', rules_dict)

    return count_matches(rules_dict, input[1])


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
