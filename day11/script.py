#!/usr/bin/python3

# puzzle input
#serial = 42
serial = 7403

# ----------------------------------------------------------------

def power_level(x, y, serial):
    rack_id = x + 10
    power_level = (rack_id * y + serial) * rack_id
    return int(str(power_level)[-3]) - 5

assert(power_level(122, 79, 57) == -5)
assert(power_level(217, 196, 39) == 0)
assert(power_level(101, 153, 71) == 4)

grid_size = 300
grid = [[power_level(x, y, serial) for y in range(grid_size)] for x in range(grid_size)]

#print(grid[:3][:3])

# ----------------------------------------------------------------

max_power = 0
max_power_pos = (0, 0)
for x in range(grid_size - 3):
    for y in range(grid_size - 3):
        power = sum(grid[x_][y_] for y_ in range(y, y + 3) for x_ in range(x, x + 3))
        if power > max_power:
            max_power = power
            max_power_pos = (x, y)

print(max_power)
print('result part one:', max_power_pos[0], max_power_pos[1])

# ----------------------------------------------------------------

max_power = 0
max_power_pos = (0, 0)
best_square_size = 0
grid_accum = [[0 for _ in range(grid_size)] for __ in range(grid_size)]
for square_size in range(1, 300):
    print('testing square size', square_size)

    for x in range(grid_size - square_size):
        for y in range(grid_size - square_size):
            for i in range(square_size - 1):
                grid_accum[x][y] += grid[x+i][y+square_size-1]
                grid_accum[x][y] += grid[x+square_size-1][y+i]
            grid_accum[x][y] += grid[x + square_size - 1][y + square_size - 1]

    for x in range(grid_size - square_size):
        for y in range(grid_size - square_size):
            if grid_accum[x][y] > max_power:
                max_power = grid_accum[x][y]
                max_power_pos = (x, y)
                best_square_size = square_size
    print('best so far:', max_power_pos[0], max_power_pos[1], best_square_size)

print('result part two:', max_power_pos[0], max_power_pos[1])
