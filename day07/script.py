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
num_workers = 2
base_time_cost = 0

# file input    
data = open('day07/input.txt').readlines()
num_workers = 5
base_time_cost = 60

# ----------------------------------------------------------------

import re

# parse all instructions into tuples
instructions = []
instr_regex = re.compile('Step ([A-Z]) must be finished before step ([A-Z]) can begin.')
for instr in data:
    r = instr_regex.match(instr)
    instructions.append((r.group(1), r.group(2)))

task_names = set(sum((list(t) for t in zip(*instructions)), []))

# ----------------------------------------------------------------

# determine starting active set == root nodes
path = []
active_set = set(instr[0] for instr in instructions if not any(cond[1] == instr[0] for cond in instructions))

# traverse with the rule set
while active_set:
    cur = chr(min(ord(letter) for letter in active_set))
    path += cur
    active_set.remove(cur)
    # add newly supported
    for task in task_names:
        if task not in path and all(cond[0] in path for cond in instructions if cond[1] == task):
            active_set.add(task)

print('result part one:', ''.join(path))

# ----------------------------------------------------------------

import operator

finished_tasks = []
tasks = set(instr[0] for instr in instructions if not any(cond[1] == instr[0] for cond in instructions))

inf = 99999999
workers = [('.', inf)] * num_workers
total_time = 0

# work!!
active_tasks = []
while tasks or active_tasks:
    # assign tasks to idle workers
    if tasks:
        for idx, _ in enumerate(workers):
            if workers[idx][0] is '.':
                new_task = chr(min(ord(letter) for letter in tasks))
                tasks.remove(new_task)
                workers[idx] = (new_task, ord(new_task) - ord('A') + 1 + base_time_cost)
                if not tasks:
                    break

    # worker with lowest workload finishes
    finished_worker = min(workers, key=operator.itemgetter(1))
    passed_time = finished_worker[1]
    total_time += passed_time

    # workers do work when time passes.
    for idx, worker in enumerate(workers):
        if worker[0] is not '.':
            time = worker[1] - passed_time
            assert(time >= 0)
            if time == 0:
                workers[idx] = ('.', inf)
                finished_tasks += finished_worker[0]
            else:
                workers[idx] = (worker[0], worker[1] - passed_time)

    # add newly available tasks to task list
    active_tasks = [worker[0] for worker in workers if worker[0] != '.']
    for task in task_names:
        if task not in finished_tasks and task not in active_tasks:
            if all(cond[0] in finished_tasks for cond in instructions if cond[1] == task):
                tasks.add(task)

print('result part two:', total_time)