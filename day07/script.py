#!/usr/bin/python3

# test input
data = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.',
]

# file input    
data = open('input.txt').readlines()

# ----------------------------------------------------------------

import re

# parse all instructions into tuples
instructions = []
instr_regex = re.compile('Step ([A-Z]) must be finished before step ([A-Z]) can begin.')
for instr in data:
    r = instr_regex.match(instr)
    instructions.append((r.group(1), r.group(2)))

# determine starting active set == root nodes
path = []
active_set = set(instr[0] for instr in instructions if not any(cond[1] == instr[0] for cond in instructions))

# traverse with the rule set
while active_set:
    cur = chr(min(ord(letter) for letter in active_set))
    path += cur
    active_set.remove(cur)
    # add newly supported
    for instr in instructions:
        if instr[0] == cur: # just became fulfilled
            checking = instr[1]
            if all(cond[0] in path for cond in instructions if cond[1] == checking):
                active_set.add(checking)

print('result part one:', ''.join(path))

# ----------------------------------------------------------------
