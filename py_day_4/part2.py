#!/usr/bin/env python3
import argparse
import re
from typing import Dict
from typing import List
from typing import Optional


def height(h: str) -> bool:
    if len(h) < 4:
        return False
    d, u = int(h[0:-2]), h[-2:]
    return (
        (u == 'cm' and d >= 150 and d <= 193) or
        (u == 'in' and d >= 59 and d <= 76)
    )


def hcl(h: str) -> bool:
    return re.fullmatch(r'#[0-9a-f]{6}', h) is not None


def ecl(h: str) -> bool:
    return h in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


CHECK = {
    'byr': lambda v: v.isnumeric() and int(v) >= 1920 and int(v) <= 2002,
    'iyr': lambda v: v.isnumeric() and int(v) >= 2010 and int(v) <= 2020,
    'eyr': lambda v: v.isnumeric() and int(v) >= 2020 and int(v) <= 2030,
    'hgt': height,
    'hcl': hcl,
    'ecl': ecl,
    'pid': lambda v: re.fullmatch(r'\d{9}', v) is not None,
    'cid': lambda v: True,
}


def validate(passport: Dict[str, str]) -> bool:
    check = 0
    for k in CHECK.keys():
        v = passport.get(k, None)
        if v is None:
            if k == 'cid':
                check += 1
            else:
                return False
        else:
            _, value = v.split(':')
            if CHECK[k](value):
                check += 1
            else:
                return False

    return check == 8


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input', nargs='?', default='input.txt',
        help='input file to read',
    )
    args = parser.parse_args()

    matcher = re.compile(
        '|'.join((
            r'(?P<NEWLINE>\n)',
            r'(?P<SPACE>\s)',
            *[fr'(?P<{f}>{f}\:[^\s]+)' for f in CHECK.keys()],
        )),
    )

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
                    if validate(curr_passport):
                        valid += 1
                    curr_passport = {}
                line_start = m.end()
            elif kind == 'SPACE':
                continue
            else:
                curr_passport[kind] = value

    # test leftovers
    if validate(curr_passport):
        valid += 1
    print(valid)
    return 0


if __name__ == '__main__':
    exit(main())
