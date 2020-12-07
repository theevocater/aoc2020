#!/usr/bin/env python3
import argparse
from typing import Dict
from typing import List
from typing import Optional


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input', nargs='?', default='input.txt',
        help='input file to read',
    )
    args = parser.parse_args()

    groups = []
    with open(args.input) as f:
        groups = [
            line.rstrip().split('\n')
            for line in f.read().split('\n\n')
        ]

    total = 0
    for group in groups:
        print(group)
        answers: Dict[str, int] = {}
        for person in group:
            for answer in person:
                answers[answer] = answers.get(answer, 0) + 1
        print(answers)
        everyone = sum([1 for v in answers.values() if v == len(group)])
        total += everyone
        print(everyone)
    print(f'total {total}')

    return 0


if __name__ == '__main__':
    exit(main())
