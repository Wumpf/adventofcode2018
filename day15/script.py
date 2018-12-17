#!/usr/bin/python3

# test input
# data_raw = [
#     '#######',
#     '#.G...#',
#     '#...EG#',
#     '#.#.#G#',
#     '#..G#E#',
#     '#.....#',
#     '#######',
# ]

# data_raw = [
#     '#######',
#     '#G..#E#',
#     '#E#E.E#',
#     '#G.##.#',
#     '#...#E#',
#     '#...E.#',
#     '#######',
# ]

# data_raw = [
#     '#######',
#     '#E..EG#',
#     '#.#G.E#',
#     '#E.##E#',
#     '#G..#.#',
#     '#..E#.#',
#     '#######',
# ]

# data_raw = [
#     '#######',
#     '#E.G#.#',
#     '#.#G..#',
#     '#G.#.G#',
#     '#G..#.#',
#     '#...E.#',
#     '#######',
# ]

# data_raw = [
#     '#######',
#     '#.E...#',
#     '#.#..G#',
#     '#.###.#',
#     '#E#G#G#',
#     '#...#G#',
#     '#######',
# ]

# data_raw = [
#     '#########',
#     '#G......#',
#     '#.E.#...#',
#     '#..##..G#',
#     '#...##..#',
#     '#...#...#',
#     '#.G...G.#',
#     '#.....G.#',
#     '#########',
# ]

# puzzle input    
data_raw = [line.strip() for line in open('day15/input.txt').readlines()]

attack_power = { 'E':3, 'G':3 }
start_hp = 200
neighbor_dirs = [(0, -1), (-1, 0), (+1, 0), (0, 1)]

# ----------------------------------------------------------------

from namedlist import namedlist
import heapq

Unit = namedlist('Unit', 'race hp x y')
unreachable = 9999999

def print_battlefield(battlefield):
    for battlefield_row in battlefield:
        units = []
        for field in battlefield_row:
            if isinstance(field, str):
                print(field, end='')
            else:
                units.append(field)
                print(field.race, end='')
        print('  ', end='')
        for unit in units:
            print(unit.race, unit.hp, ' ', end='')
        print()

#print_battlefield(battlefield)

def get_adjacent_enemies(battlefield, unit):
    enemies = []
    for d in neighbor_dirs:
        field = battlefield[unit.y + d[1]][unit.x + d[0]]
        if not isinstance(field, str):
            if field.race != unit.race:
                assert(field.hp > 0)
                enemies.append(field)
    return enemies


def dijkstra(battlefield, start):
    distances = [[unreachable for x in range(len(battlefield[0]))] for y in range(len(battlefield))] 
    visited = [[False for x in range(len(battlefield[0]))] for y in range(len(battlefield))]

    distances[start[1]][start[0]] = 0
    queue = [(0, start[0], start[1])]

    while len(queue) > 0:
        c, x, y = heapq.heappop(queue)
        if not visited[y][x]:
            visited[y][x] = True
            newdist = 1 + c
            for d in neighbor_dirs:
                xn = x + d[0]
                yn = y + d[1]
                if battlefield[yn][xn] != '.':
                    continue
                if distances[yn][xn] > newdist:
                    distances[yn][xn] = newdist
                    heapq.heappush(queue, (newdist, xn, yn)) # instead of updating old items, just keep pushing
    return distances


def game(part2):
    num_units = {'G': 0, 'E': 0}
    battlefield = []
    for y, row in enumerate(data_raw):
        battlefield_row = []
        battlefield.append(battlefield_row)
        for x, letter in enumerate(row):
            if letter == 'G' or letter == 'E':
                battlefield_row.append(Unit(race=letter, hp=start_hp, x=x, y=y))
                num_units[letter] += 1
            else:
                battlefield_row.append(letter)

    battling = True
    finished_rounds = 0
    while battling:
        finished_rounds += 1
        units = []
        for battlefield_row in battlefield:
            for field in battlefield_row:
                if not isinstance(field, str):
                    units.append(field)
        
        for unit in units:
            if unit.hp <= 0:
                continue
            if not battling:
                finished_rounds -= 1
                break

            # check if move is skipped because there is already an enemy
            enemies = get_adjacent_enemies(battlefield, unit)
            if len(enemies) == 0:
                # move phase
                distances = dijkstra(battlefield, (unit.x, unit.y))
                potential_targets = [(d[0] + enemy.x, d[1] + enemy.y) for d in neighbor_dirs for enemy in units if enemy.race != unit.race and enemy.hp > 0]
                potential_targets.sort(key=lambda t: t[0])
                potential_targets.sort(key=lambda t: t[1])
                potential_targets.sort(key=lambda t: distances[t[1]][t[0]])
                target = potential_targets[0]
                if distances[target[1]][target[0]] != unreachable:

                    distances = dijkstra(battlefield, target)

                    move_target = min(((unit.x + d[0], unit.y + d[1]) for d in neighbor_dirs), key=lambda p: distances[p[1]][p[0]])
                    xm, ym = move_target
                    if distances[ym][xm] != unreachable:
                        assert(battlefield[ym][xm] == '.')
                        battlefield[ym][xm] = unit
                        battlefield[unit.y][unit.x] = '.'
                        unit.x, unit.y = move_target
                        enemies = get_adjacent_enemies(battlefield, unit)

            # attack phase
            if len(enemies) > 0:
                enemies.sort(key=lambda enemy: enemy.hp)
                target = enemies[0]
                assert(target.hp > 0)
                target.hp -= attack_power[unit.race]
                if target.hp <= 0:
                    battlefield[target.y][target.x] = '.'
                    num_units[target.race] -= 1
                    #print(target.race, 'died')
                    battling = num_units[target.race] != 0

                    if part2 and target.race == 'E':
                        print('elves lost')
                        return False

    score = finished_rounds * sum(unit.hp for unit in units if unit.hp > 0)
    return score

#print_battlefield(battlefield)
print('outcome', game(False))

attack_power['E'] += 1
result = game(True)
while result == False:
    attack_power['E'] += 1
    result = game(True)
print('outcome', result)
