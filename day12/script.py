#!/usr/bin/python3

# test input
# data_raw = open('day12/testinput.txt').readlines()

# puzzle input    
data_raw = open('day12/input.txt').readlines()
num_generations = 20

# ----------------------------------------------------------------

state = list(data_raw[0].split(' ')[2].strip())

rules = set()
for line in data_raw[2:]:
    parts = line.split(' ')
    if parts[-1].strip() == '#':
        rules.add(parts[0].strip())
print(rules)

liststart = 0
potsums = []
stablegrowthsince = 0
last_delta = 0
for gen in range(999999):
    if state[0] == '#':
        state = ['.'] * 3 + state
        liststart -= 3
    elif state[1] == '#':
        state = ['.'] * 2 + state
        liststart -= 2
    elif state[2] == '#':
        state = ['.'] * 1 + state
        liststart -= 1
    if state[-1] == '#':
        state.extend(['.'] * 3)
    elif state[-2] == '#':
        state.extend(['.'] * 2)
    elif state[-3] == '#':
        state.extend(['.'])

    new_state = ['.'] * len(state)
    for i in range(2, len(state) - 2):
        key = ''.join(state[i-2:i+3])
        if key in rules:
            new_state[i] = '#'
    state = new_state

    potsums.append(sum(i + liststart for i, v in enumerate(state) if v == '#'))
    if len(potsums) > 10:
        delta = potsums[-1] - potsums[-2]
        if delta == last_delta:
            stablegrowthsince += 1
        else:
            stablegrowthsince = 0
        last_delta = delta

        if stablegrowthsince > 10:
            print('generation:', gen)
            print('stable_delta:', delta)
            print('result part two:', potsums[-1] + delta * (50000000000 - gen - 1))
            break

print('result part one:', potsums[num_generations-1])
