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
        inputs = [int(line.rstrip()) for line in f]

    target = 2020
    seen = set()
    for i in inputs:
        seen.add(i)
        pair = target - i
        if pair in seen:
            print(f'{i} + {pair} = {target}, {i*pair}')

    return 0


if __name__ == '__main__':
    exit(main())
