#!/usr/bin/env python3
import argparse
import math
from typing import List
from typing import Optional


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input', nargs='?', default='input.txt',
        help='input file to read',
    )
    args = parser.parse_args()

    inputs = []
    with open(args.input) as f:
        inputs = [line.rstrip() for line in f]

    max_seat_id = 0
    for seat_code in inputs:
        min = 0
        max = 127
        for letter in seat_code[0:7]:
            if letter == 'F':
                # keep 'front'
                max = max - math.ceil((max - min) / 2)
                row = min
            if letter == 'B':
                # keep 'back'
                min = min + math.ceil((max - min) / 2)
                row = max
            # print(f'{letter} {min} {max}')
        min = 0
        max = 7
        for letter in seat_code[7:10]:
            if letter == 'L':
                max = max - math.ceil((max - min) / 2)
                seat = max
            if letter == 'R':
                min = min + math.ceil((max - min) / 2)
                seat = min
            # print(f'{letter} {min} {max}')

        seat_id = row * 8 + seat
        if seat_id > max_seat_id:
            max_seat_id = seat_id
        print(f'{seat_code} {row}:{seat} {seat_id}')

    print(f'max seat_id = {max_seat_id}')

    return 0


if __name__ == '__main__':
    exit(main())
