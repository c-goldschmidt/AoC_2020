import re

from utils import run

rx_rule = re.compile(r'^(?P<num>\d+): (?P<rules>.+)$')


class Rule:

    def __init__(self, content, rules_dict):
        self.rules_dict = rules_dict
        self.match_char = None
        self.match_rules = None
        self.match_cache = {}

        parts = [item for item in content.split(' | ') if item]
        if len(parts) == 1 and '"' in parts[0]:
            self.match_char = parts[0][1:2]
        else:
            self.match_rules = [[rule for rule in part.split(' ')] for part in parts]

    def matches(self, str_in):
        if str_in not in self.match_cache:
            self.match_cache[str_in] = []  # recursion catcher
            self.match_cache[str_in] = self._matches(str_in)
        return self.match_cache[str_in]

    def _matches(self, str_in):
        if not str_in:
            return []

        if self.match_char:
            return [str_in[1:]] if str_in[0] == self.match_char else []
        else:
            possible_matches = []
            for rule in self.match_rules:
                possible_matches += self.match_sub_rules(str_in, rule)

            return possible_matches

    def match_sub_rules(self, str_in, rule):
        rule_matches = [[str_in]]

        for index, sub_rule in enumerate(rule):
            if not rule_matches:
                return []

            if len(rule_matches) == index + 1:
                rule_matches.append([])

            for item in rule_matches[index]:
                rule_matches[index + 1] += self.rules_dict[sub_rule].matches(item)

        return rule_matches[index + 1]


def get_input(content):
    split = content.split('\n\n')
    return (
        [rx_rule.search(line) for line in split[0].split('\n') if line],
        [line for line in split[1].split('\n') if line],
    )


def count_matches(rules_dict, messages):
    num_matching = 0
    for message in messages:
        matches = [item for item in rules_dict['0'].matches(message) if item == '']
        num_matching += 1 if matches else 0
    return num_matching


def create_rules_dict(rules_list):
    rules_dict = {}
    for rule in rules_list:
        rules_dict[rule['num']] = Rule(rule['rules'], rules_dict)
    return rules_dict


def get_answer(input):
    rules_dict = create_rules_dict(input[0])
    return count_matches(rules_dict, input[1])


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
