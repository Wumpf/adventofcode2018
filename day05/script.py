#!/usr/bin/python3

# test input
#data = 'dabAcCaCBAcCcaDA'

# file input
data = open('input.txt').read()

# ----------------------------------------------------------------

def collapse(units):
    polymer = [units[0]]
    for unit in units[1:]:
        if polymer and unit != polymer[-1] and unit.lower() == polymer[-1].lower():
            polymer.pop()
        else:
            polymer.append(unit)
    return polymer

# ----------------------------------------------------------------

print('result part one:', len(collapse(data)))

# ----------------------------------------------------------------

shortest = 9999999
for letter in range(ord('a'), ord('z') + 1):
    polymer = collapse(data.replace(chr(letter), '').replace(chr(letter).upper(), ''))
    shortest = min(shortest, len(polymer))

print('result part two:', shortest)
