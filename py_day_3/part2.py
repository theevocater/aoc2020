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

    velocities = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1),
    ]
    trees = []
    for rv, cv in velocities:
        r = 0
        c = 0
        tree = 0
        while r < len(inputs):
            spot = inputs[r][c]
            if spot == '#':
                tree += 1
            c += cv
            if c >= len(inputs[r]):
                c = c - len(inputs[r])
            r += rv
        trees.append(tree)

    print(f'{trees} {math.prod(trees)}')
    return 0


if __name__ == '__main__':
    exit(main())
