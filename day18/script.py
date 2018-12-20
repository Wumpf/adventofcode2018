#!/usr/bin/python3

# test input
data_raw = [
    '.#.#...|#.',
    '.....#|##|',
    '.|..|...#.',
    '..|#.....#',
    '#.#|||#|#|',
    '...#.||...',
    '.|....|...',
    '||...#|.#|',
    '|.||||..|.',
    '...#.|..|.',
]

# puzzle input
data_raw = [line.strip() for line in open('day18/input.txt').readlines()]

# ----------------------------------------------------------------

state = [list(row) for row in data_raw]

def count_adjacent(looking_for, x, y, state):
    minx = max(x-1, 0)
    maxx = min(x+2, len(state[0]))
    miny = max(y-1, 0)
    maxy = min(y+2, len(state))
    return sum(thing == looking_for for row in state[miny:maxy] for thing in row[minx:maxx]) - (state[y][x] == looking_for)

history = []
num_minutes = 1000000000
i = 0
while i < num_minutes:
    history.append(state)
    new_state = [row.copy() for row in state]
    for y in range(len(state)):
        for x in range(len(state[0])):
            if state[y][x] == '.':
                if count_adjacent('|', x, y, state) >= 3:
                    new_state[y][x] = '|'
            elif state[y][x] == '|':
                if count_adjacent('#', x, y, state) >= 3:
                    new_state[y][x] = '#'
            else: #if state[y][x] == '#':
                if count_adjacent('#', x, y, state) == 0 or count_adjacent('|', x, y, state) == 0:
                    new_state[y][x] = '.'
    state = new_state
    i += 1

    if state in history:
        repeated_at = history.index(state)
        print('state at minute', i, 'is equal to', repeated_at)
        interval = i - repeated_at
        i += int((num_minutes - i) / interval) * interval
        print('jump i to', i)
        history = []

num_wood = sum(x == '|' for row in state for x in row )
num_lumber = sum(x == '#' for row in state for x in row)
print('result part two:', num_lumber * num_wood)