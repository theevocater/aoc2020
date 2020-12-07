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

    with open(args.input) as f:
        print(
            sum([
                len(set(line.replace('\n', '')))
                for line in f.read().split('\n\n')
            ]),
        )

    return 0


if __name__ == '__main__':
    exit(main())
