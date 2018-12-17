#!/usr/bin/python3

# test input
# data_raw = [
#     'x=495, y=2..7',
#     'y=7, x=495..501',
#     'x=501, y=3..7',
#     'x=498, y=2..4',
#     'x=506, y=1..2',
#     'x=498, y=10..13',
#     'x=504, y=10..13',
#     'y=13, x=498..504',
# ]

# puzzle input
data_raw = [line.strip() for line in open('day17/input.txt').readlines()]

spring = (500, 0)

# ----------------------------------------------------------------

import re

areamin = (9999999, 9999999)
areamax = (0, 0)
ground = [['.' for x in range(2000)] for y in range(2000)]

parse_re = re.compile('([xy])=(\d+), [xy]=(\d+)..(\d+)')
for line in data_raw:
    r = parse_re.match(line)
    if r.group(1) == 'x':
        x = int(r.group(2))
        ymin = int(r.group(3))
        ymax = int(r.group(4))
        areamin = (min(areamin[0], x), min(areamin[1], ymin))
        areamax = (max(areamax[0], x), max(areamax[1], ymax))
        for y in range(ymin, ymax + 1):
            ground[y][x] = '#'
    else:
        y = int(r.group(2))
        xmin = int(r.group(3))
        xmax = int(r.group(4))
        areamin = (min(areamin[0], xmin), min(areamin[1], y))
        areamax = (max(areamax[0], xmax), max(areamax[1], y))
        for x in range(xmin, xmax + 1):
            ground[y][x] = '#'
print(areamin, areamax)

def draw():
    for row in ground[areamin[1]:areamax[1] + 1]:
        for field in row[areamin[0]-1:areamax[0] + 2]:
            print(field, end='')
        print()


def is_bounded_in(y, xrange):
    for x in xrange:
        if ground[y][x] == '#':
            return x
        below = ground[y + 1][x]
        if below != '#' and below != '~':
            return None
    return None


def trickledown(x, y):
    stack = [(x,y)]

    while len(stack) > 0:
        x, y = stack.pop()
        if y > areamax[1]:
            continue
        if ground[y][x] == '.':
            ground[y][x] = '|'
            stack.append((x, y))
            stack.append((x, y + 1))
            continue

        below = ground[y + 1][x]
        if below == '#' or below == '~':
            bounded_right = is_bounded_in(y, range(x, len(ground[0])))
            if bounded_right != None:
                bounded_left = is_bounded_in(y, range(x-1, 0, -1))
                if bounded_left != None:
                    ground[y][bounded_left+1:bounded_right] = ['~'] * (bounded_right - bounded_left - 1)
                    continue
            if ground[y][x+1] == '.':
                stack.append((x+1, y))
            if ground[y][x-1] == '.':
                stack.append((x-1, y))


trickledown(spring[0], spring[1])
draw()

num_wet_fields = sum(field == '~' or field == '|' for row in ground[areamin[1]:areamax[1] + 1] for field in row[areamin[0]-1:areamax[0] + 2])
print('result part one:', num_wet_fields)
num_watery = sum(field == '~' for row in ground[areamin[1]:areamax[1] + 1] for field in row[areamin[0]-1:areamax[0] + 2])
print('result part two:', num_watery)