#!/usr/bin/python3

# test input
data = [
    'position=< 9,  1> velocity=< 0,  2>',
    'position=< 7,  0> velocity=<-1,  0>',
    'position=< 3, -2> velocity=<-1,  1>',
    'position=< 6, 10> velocity=<-2, -1>',
    'position=< 2, -4> velocity=< 2,  2>',
    'position=<-6, 10> velocity=< 2, -2>',
    'position=< 1,  8> velocity=< 1, -1>',
    'position=< 1,  7> velocity=< 1,  0>',
    'position=<-3, 11> velocity=< 1, -2>',
    'position=< 7,  6> velocity=<-1, -1>',
    'position=<-2,  3> velocity=< 1,  0>',
    'position=<-4,  3> velocity=< 2,  0>',
    'position=<10, -3> velocity=<-1,  1>',
    'position=< 5, 11> velocity=< 1, -2>',
    'position=< 4,  7> velocity=< 0, -1>',
    'position=< 8, -2> velocity=< 0,  1>',
    'position=<15,  0> velocity=<-2,  0>',
    'position=< 1,  6> velocity=< 1,  0>',
    'position=< 8,  9> velocity=< 0, -1>',
    'position=< 3,  3> velocity=<-1,  1>',
    'position=< 0,  5> velocity=< 0, -1>',
    'position=<-2,  2> velocity=< 2,  0>',
    'position=< 5, -2> velocity=< 1,  2>',
    'position=< 1,  4> velocity=< 2,  1>',
    'position=<-2,  7> velocity=< 2, -2>',
    'position=< 3,  6> velocity=<-1, -1>',
    'position=< 5,  0> velocity=< 1,  0>',
    'position=<-6,  0> velocity=< 2,  0>',
    'position=< 5,  9> velocity=< 1, -2>',
    'position=<14,  7> velocity=<-2,  0>',
    'position=<-3,  6> velocity=< 2, -1>',
]
# file input
#data = open('day10/input.txt').readlines()

# ----------------------------------------------------------------

import re

regex = re.compile('position=<(.+),(.+)> velocity=<(.+),(.+)>')
positions = []
velocities = []
for line in data:
    r = regex.match(line)
    positions.append((int(r.group(1)), int(r.group(2))))
    velocities.append((int(r.group(3)), int(r.group(4))))

# ----------------------------------------------------------------

import matplotlib.pyplot as plt
import itertools

for step in itertools.count():
    positions = list((p[0] + v[0], p[1] + v[1]) for p,v in zip(positions, velocities))

    positions_sorted = sorted(positions)

    prev = positions_sorted[0]
    vlinelen = 0
    for p in positions_sorted[1:]:
        if prev[0] == p[0]:
            vlinelen += 1
            if vlinelen > 5:
                print (f'plotting step {step+1}')
                plt.plot(list(p[0] for p in positions), list(p[1] for p in positions), 'ro')
                plt.show()
                break
        else:
            vlinelen = 0
        prev = p
