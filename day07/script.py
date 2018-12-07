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
#data = open('input.txt').readlines()

# ----------------------------------------------------------------

import re

instructions = []
instr_regex = re.compile('Step ([A-Z]) must be finished before step ([A-Z]) can begin.')
for instr in data:
    r = instr_regex.match(instr)
    instructions.append((r.group(1), r.group(2)))


tree = { instr[0]:[] for instr in instructions }


# ----------------------------------------------------------------
