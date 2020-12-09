from day_9.part1 import get_answer as inv_code, get_input
from utils import run


def get_answer(input):
    invalid = inv_code(input)

    sums = []
    for i in range(0, len(input)):
        sums.append([input[i]])

        for j in range(0, i):
            if not sums[j]:
                continue
            sums[j].append(input[i])

            if sum(sums[j]) == invalid:
                sums[j].sort()
                return sums[j][0] + sums[j][-1]

            if sum(sums[j]) > invalid:
                sums[j] = None
    return -1


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
