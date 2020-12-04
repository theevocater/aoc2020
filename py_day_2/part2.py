#!/usr/bin/env python3
import argparse
import re
from typing import List
from typing import Optional


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input', nargs='?', default='input.txt',
        help='input file to read',
    )
    args = parser.parse_args()

    matcher = (
        r'(?P<start>\d+)-(?P<end>\d+)'
        r' (?P<letter>[a-z]): '
        r'(?P<password>.+)'
    )

    inputs = []
    with open(args.input) as f:
        inputs = [line.rstrip() for line in f]

    valid = 0
    for i in inputs:
        m = re.fullmatch(matcher, i)
        if m is None:
            raise RuntimeError(f'failed to match {i}')
        start, end, letter, password = m.groups()

        pos1 = int(start) - 1
        pos2 = int(end) - 1

        space = f'{letter} {password[pos1]} {password[pos2]}'
        if (
                (password[pos1] == letter and password[pos2] != letter) or
                (password[pos1] != letter and password[pos2] == letter)
        ):
            print(f'VALID {space}')
            valid += 1
        else:
            print(f'NOT {space}')

    print(f'{valid} out of {len(inputs)}')

    return 0


if __name__ == '__main__':
    exit(main())
