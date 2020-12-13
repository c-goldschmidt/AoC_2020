from day_13.part1 import get_input
from utils import run


def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_euclidean(b % a, a)
        return g, x - (b // a) * y, y


def inverse_mod(a, m):
    g, x, y = extended_euclidean(a, m)
    return x % m


# The chinese remainder theorem
def chi_rem_thm(m, x):
    while True:
        temp1 = inverse_mod(m[1], m[0]) * x[0] * m[1] + inverse_mod(m[0], m[1]) * x[1] * m[0]
        temp2 = m[0] * m[1]

        x.remove(x[0])
        x.remove(x[0])
        x = [temp1 % temp2] + x

        m.remove(m[0])
        m.remove(m[0])
        m = [temp2] + m

        if len(x) == 1:
            return x[0]


def get_answer(input):
    values = []
    remainders = []

    for i, value in enumerate(input[1]):
        if value == 'x':
            continue

        values.append(int(value))
        if i == 0:
            remainders.append(0)
        else:
            remainders.append(int(value) - i)

    return chi_rem_thm(values, remainders)


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
