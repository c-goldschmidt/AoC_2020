import argparse
from datetime import datetime

from utils import run_day

if __name__ == '__main__':
    # run specific day, runs both parts.
    # runs current day if no --day given
    parser = argparse.ArgumentParser()
    parser.add_argument('--day', type=int)
    ns = parser.parse_args()

    if ns.day:
        run_day(ns.day)
    else:
        run_day(datetime.now().day)
