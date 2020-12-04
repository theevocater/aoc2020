#!/usr/bin/env python3
import argparse
import re
from typing import Dict
from typing import List
from typing import Optional
from typing import Set


def validate(passport: Dict[str, str], fields: Set[str]) -> bool:
    keys = set(passport.keys())
    diff = fields - keys
    ret = len(diff) == 0 or (len(diff) == 1 and 'cid' in diff)
    if not ret:
        print(diff)
    return ret


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input', nargs='?', default='input.txt',
        help='input file to read',
    )
    args = parser.parse_args()

    fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        'cid',
    }

    matcher = re.compile(
        '|'.join((
            r'(?P<NEWLINE>\n)',
            r'(?P<SPACE>\s)',
            *[fr'(?P<{f}>{f}\:[^\s]+)' for f in fields],
        )),
    )
    print(matcher)

    valid = 0
    with open(args.input) as f:
        line_num = 0
        line_start = 0
        curr_passport: Dict[str, str] = {}
        for m in re.finditer(matcher, f.read()):
            kind = m.lastgroup
            if not kind:
                raise RuntimeError('failed to match kind')
            value = m.group()
            column = m.start() - line_start
            if kind == 'NEWLINE':
                line_num += 1
                if column == 0:
                    if validate(curr_passport, fields):
                        valid += 1
                    else:
                        print(f'{len(curr_passport.keys())} {curr_passport}')
                    curr_passport = {}
                line_start = m.end()
            elif kind == 'SPACE':
                continue
            else:
                curr_passport[kind] = value

    # test leftovers
    if validate(curr_passport, fields):
        valid += 1
    else:
        print(f'{len(curr_passport.keys())} {curr_passport}')
    print(valid)
    return 0


if __name__ == '__main__':
    exit(main())
