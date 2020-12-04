#!/usr/bin/env python3
import argparse
from typing import List
from typing import Optional
from typing import Set


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
    seen: Set[int] = set()
    for i in inputs:
        sub_target = target - i
        for s in seen:
            pair = sub_target - s
            if pair in seen:
                print(f'{i} + {s} + {pair} = {target}, {i*s*pair}')
                break
        seen.add(i)

    return 0


if __name__ == '__main__':
    exit(main())
