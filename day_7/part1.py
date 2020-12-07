import re

from utils import run

rx_data = re.compile(r'^(?P<parent>.+?) bags contain (?P<contents>.+)$', re.MULTILINE)
rx_content = re.compile(r'(?P<num>\d+) (?P<color>\w+ \w+) bags?')


def get_input(content):
    return rx_data.finditer(content)


class Node:
    def __init__(self, name, num=None, content=None):
        self.name = name
        self.num = num
        self.filled = False
        self.children = self.parse(content) if content else []

    @staticmethod
    def parse(content):
        children = []
        for item in rx_content.finditer(content):
            children.append(Node(item.group('color'), num=int(item.group('num'))))
        return children


def find_parents(nodes, color):
    found = set()
    for node in nodes:
        contained = [child for child in node.children if child.name == color]
        if contained:
            found.add(node)
            found |= find_parents(nodes, node.name)

    return found


def get_answer(input):
    nodes = []
    for item in input:
        nodes.append(Node(item.group('parent'), content=item.group('contents')))

    parents = find_parents(nodes, 'shiny gold')
    return len(parents)


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
