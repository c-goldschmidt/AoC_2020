from time import time

from utils import run


def get_input(content):
    players = content.split('\n\n')
    return (
        [int(line) for line in players[0].split('\n')[1:] if line],
        [int(line) for line in players[1].split('\n')[1:] if line],
    )


def play_round(p1, p2):
    card1 = p1.pop(0)
    card2 = p2.pop(0)

    if card1 > card2:
        p1 += [card1, card2]
    else:
        p2 += [card2, card1]


def play_game(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        play_round(p1, p2)


def calc_score(winner):
    total = 0
    for i in range(1, len(winner) + 1):
        total += winner[-i] * i
    return total


def get_answer(input):
    p1, p2 = input
    play_game(p1, p2)
    return calc_score(p1 or p2)


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
