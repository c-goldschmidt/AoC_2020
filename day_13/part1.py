from utils import run


def get_input(content):
    split = content.split('\n')
    return int(split[0]), split[1].split(',')


def get_answer(input):
    timestamp = input[0] - 1
    bus_id = None
    while not bus_id:
        timestamp += 1
        for item in input[1]:
            if item == 'x':
                continue

            if timestamp % int(item) == 0:
                bus_id = int(item)

    return bus_id * (timestamp - input[0])


if __name__ == '__main__':
    run(__file__, get_input, get_answer)
