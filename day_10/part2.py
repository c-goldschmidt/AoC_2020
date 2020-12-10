from day_10.part1 import get_input
from utils import run


def get_answer(input):
    input.sort()
    input = [0] + input + [max(input) + 3]
    streak = 0
    streaks = []

    for i, value in enumerate(input):
        if i == 0:
            continue

        prev = input[i - 1]
        diff = value - prev

        if diff == 1:
            streak += 1
        else:
            if streak > 1:
                streaks.append(streak - 1)
            streak = 0

    total = 1
    for i in streaks:
        streak_val = 2 ** i
        if i == 3:
            # cannot replace all 3, as that would increase the maximum distance to 4
            streak_val -= 1
        total *= streak_val

    return total


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
