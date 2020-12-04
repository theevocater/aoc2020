#!/usr/bin/env python3
import argparse
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

    r = 0
    c = 0
    trees = 0
    while r < len(inputs):
        spot = inputs[r][c]
        if spot == '#':
            trees += 1
        c += 3
        if c >= len(inputs[r]):
            c = c - len(inputs[r])
        r += 1

    print(trees)
    return 0


if __name__ == '__main__':
    exit(main())
