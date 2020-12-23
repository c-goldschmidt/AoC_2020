from utils import run


def get_input(content):
    cups = [Cup(num) for num in content.split('\n')[0]]
    for i, cup in enumerate(cups):
        cup.next = cups[(i + 1) % len(cups)]
        cup.prev = cups[i - 1]

    return cups[0]


class Cup:
    def __init__(self, value):
        self.value = int(value)
        self.prev = None
        self.next = None

    def to_list(self):
        cups = [self]
        next_cup = self.next
        while next_cup != self:
            cups.append(next_cup)
            next_cup = next_cup.next
        return cups

    def __str__(self):
        return str(self.value)

    def min(self):
        return min([item.value for item in self.to_list()])

    def max(self):
        return max([item.value for item in self.to_list()])


def move(current_cup, min_value, max_value, cup_by_value):
    pick_up = [
        current_cup.next,
        current_cup.next.next,
        current_cup.next.next.next,
    ]
    destination = get_dest_cup(current_cup, pick_up, min_value, max_value, cup_by_value)

    dest_next = destination.next
    pickup_next = pick_up[-1].next
    pickup_prev = pick_up[0].prev

    # move pick_up next to dest
    pick_up[0].prev = destination
    destination.next = pick_up[0]

    # move previous destination.next to end of pick up
    pick_up[-1].next = dest_next
    dest_next.prev = pick_up[-1]

    # link elements before removal and after removal
    pickup_prev.next = pickup_next
    pickup_next.prev = pickup_prev

    return current_cup.next


def get_dest_cup(current_cup, pick_up, min_value, max_value, cup_by_value):
    pick_up_values = [cup.value for cup in pick_up]
    destination_value = current_cup.value - 1

    while not destination_value or destination_value in pick_up_values:
        if destination_value - 1 >= min_value:
            destination_value -= 1
        else:
            destination_value = max_value

    return cup_by_value[destination_value]


def run_for_moves(input, moves):
    current = input
    min_value = current.min()
    max_value = current.max()
    cup_by_value = {cup.value: cup for cup in current.to_list()}

    for i in range(moves):
        current = move(current, min_value, max_value, cup_by_value)

    return cup_by_value[1]


def get_answer(input):
    cup_1 = run_for_moves(input, 100)
    return ''.join(str(cup) for cup in cup_1.to_list()[1:])


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
