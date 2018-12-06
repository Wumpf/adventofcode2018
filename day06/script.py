#!/usr/bin/python3

# test input
data = [
    '1, 1',
    '1, 6',
    '8, 3',
    '3, 4',
    '5, 5',
    '8, 9',
]
max_total_dist = 32
board_size = 20

# file input
data = open('input.txt').readlines()
max_total_dist = 10000
board_size = 500

# ----------------------------------------------------------------

coordinates = [tuple(int(num) for num in line.split(',')) for line in data]
# ----------------------------------------------------------------

def find_closest_cor(x, y):
    dist = float("inf")
    closest = 0
    for idx, cor in enumerate(coordinates):
        d = abs(x - cor[0]) + abs(y - cor[1])
        if dist > d:
            closest = idx
            dist = d
        elif dist == d:
            closest = len(coordinates)
    return closest

board = [[find_closest_cor(x, y) for x in range(board_size)] for y in range(board_size)]
scores = [sum(field == i for row in board for field in row) for i in range(len(coordinates))]

scores.append(0) # for overlapping
for i in range(board_size):
    scores[board[i][0]] = 0
    scores[board[0][i]] = 0
    scores[board[-1][i]] = 0
    scores[board[i][-1]] = 0
scores.pop()

print('result part one:', max(scores))

# ----------------------------------------------------------------

board = [[sum(abs(x - cor[0]) + abs(y - cor[1]) for cor in coordinates) for x in range(board_size)] for y in range(board_size)]
print('result part two:', sum(field < max_total_dist for row in board for field in row))

