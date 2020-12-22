from day_22.part1 import get_input, calc_score
from utils import run


def play_round(p1, p2, states, depth):
    state_hash = hash(f'{p1}/{p2}')
    if state_hash in states:
        # state seen, infinite recursion.
        raise RecursionError()
    states.add(state_hash)

    card1 = p1.pop(0)
    card2 = p2.pop(0)

    if len(p1) >= card1 and len(p2) >= card2:
        clone1 = [card for i, card in enumerate(p1) if i < card1]
        clone2 = [card for i, card in enumerate(p2) if i < card2]
        p1_wins = play_game(clone1, clone2, depth + 1)
    else:
        p1_wins = card1 > card2

    if p1_wins:
        p1 += [card1, card2]
    else:
        p2 += [card2, card1]

    return p1_wins


def play_game(p1, p2, depth=1):
    states = set()
    try:
        while len(p1) > 0 and len(p2) > 0:
            play_round(p1, p2, states, depth)
        return len(p1) > len(p2)
    except RecursionError:
        # player 1 wins game by infinite recursion
        return True


def get_answer(input):
    p1, p2 = input
    p1_wins = play_game(p1, p2)
    return calc_score(p1 if p1_wins else p2)


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
