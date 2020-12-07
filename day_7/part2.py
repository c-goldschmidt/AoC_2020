from day_7.part1 import Node, get_input
from utils import run


def count_children(nodes, parent_name):
    node = [node for node in nodes if node.name == parent_name]
    if not node:
        raise Exception(f"did not find {parent_name}")

    bag_count = 0
    for child in node[0].children:
        bag_count += child.num
        bag_count += child.num * count_children(nodes, child.name)
    return bag_count


def get_answer(input):
    nodes = []
    for item in input:
        nodes.append(Node(item.group('parent'), content=item.group('contents')))

    return count_children(nodes, 'shiny gold')


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
