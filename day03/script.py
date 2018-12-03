#!/usr/bin/python3
import re

# test input
# data = [
# '#1 @ 1,3: 4x4',
# '#2 @ 3,1: 4x4',
# '#3 @ 5,5: 2x2',
# ]
# size = 9

# file input
data = open('input.txt').readlines()
size = 1000

# ----------------------------------------------------------------

nonoverlapping_ids = set()
area = [['.' for x in range(size)] for y in range(size)]
claim_regex = re.compile('#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)')
for claim in data:
    r = claim_regex.match(claim)
    nonoverlapping = True
    for x in range(int(r.group('x')), int(r.group('x')) + int(r.group('w'))):
        for y in range(int(r.group('y')), int(r.group('y')) + int(r.group('h'))):
            if area[x][y] == '.':
                area[x][y] = r.group('id')
            else:
                nonoverlapping = False
                try:
                    nonoverlapping_ids.remove(area[x][y])
                except KeyError:
                    pass
                area[x][y] = 'x'
    if nonoverlapping:
        nonoverlapping_ids.add(r.group('id'))


print('result part one:', sum([row.count('x') for row in area]))
print('result part two:', nonoverlapping_ids)